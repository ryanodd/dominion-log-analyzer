from logAnalyzer.boonsAndHexesAndStates import getBoonOrHexOrState
from logAnalyzer.logParser.strings import *  # all prefixed with s_ or r_
from logAnalyzer.logParser.cardNameFilter import getFilteredCardName
from logAnalyzer.game import Game, Player
from logAnalyzer.utils.logger import logErrorAndRaise
from logAnalyzer.utils.pythonUtils import removeItemsFromList

# Takes in 2 lists of words (str/regexp) and returns T/F if matching
# Works on both strings and regexps
# ignores trailing commas or periods


def validateWordSequence(testWords, referenceWords):
    for wordIndex in range(len(testWords)):
        testString = testWords[wordIndex]
        if testString[-1] == '.' or testString[-1] == ',':
            testString = testString[0:-1]
        if callable(getattr(referenceWords[wordIndex], 'match', None)):
            # Regular Experession
            if not referenceWords[wordIndex].match(testString):
                return False
        else:
            # String
            if testString != referenceWords[wordIndex]:
                return False
    return len(testWords) == len(referenceWords)

# Looks for an exact match with the words given.
# This only adds spaces and removes commas/periods


def parseSingleCardFromStrings(words):
    nameString = " ".join(words)
    if nameString[-1] == '.' or nameString[-1] == ',':
        nameString = nameString[0:-1]
    return getFilteredCardName(nameString)


def parseBoonOrHexOrStateFromStrings(words):
    nameString = " ".join(words)
    if nameString[-1] == '.' or nameString[-1] == ',':
        nameString = nameString[0:-1]
    return getBoonOrHexOrState(nameString)


def parseMultipleCardsFromStrings(words, firstWordIndex, lastWordIndex=99999, stopWords=[]):
    if lastWordIndex < len(words):
        words = words[firstWordIndex:lastWordIndex+1]
    else:
        words = words[firstWordIndex:]
    listToReturn = []
    "2 Coppers, a Bridge, a Bridge Troll, an Estate, and a Jack of All Trades."
    loopIndex = 0
    while loopIndex < len(words):

        if words[loopIndex] in stopWords:
            return listToReturn

        if parseBoonOrHexOrStateFromStrings(words[loopIndex:len(words)]) is not None:
            return listToReturn

        # Skip 'and'
        if words[loopIndex] == s_and:
            loopIndex += 1

        # Determine quantity
        qtyString = words[loopIndex]
        if r_number.match(qtyString):
            cardQuantity = int(qtyString)
        elif qtyString == s_a or qtyString == s_an:
            cardQuantity = 1
        else:
            logErrorAndRaise(
                'Couldn\'t determine quantity: ' + qtyString)
        loopIndex += 1  # processed quantity

        # check for stop words again, sometimes they come after 'a'
        # e.g. J sets a card aside with Library
        if words[loopIndex] in stopWords:
            return listToReturn

        # loop, adding words until we know we can't
        nameBeginIndex = loopIndex
        while(loopIndex < len(words)):
            if parseSingleCardFromStrings(words[nameBeginIndex:loopIndex+1]) is not None\
                    and not (loopIndex + 1 < len(words) and parseSingleCardFromStrings(words[nameBeginIndex:loopIndex+2]) is not None):
                break
            loopIndex += 1

        cardName = parseSingleCardFromStrings(
            words[nameBeginIndex:loopIndex+1])
        if (cardName is None):
            logErrorAndRaise('Could not find card name: ' +
                             " ".join(words[nameBeginIndex:loopIndex+1]))
        listToReturn += ([cardName] * cardQuantity)
        loopIndex += 1
    return listToReturn


def logToGame(logString):

    game = Game()

    lines = logString.split('\n')
    for line in lines:
        words = line.split()
        functionToCall = getFunctionForLine(words, game)
        if functionToCall is not None:
            functionToCall(words, game)  # get & execute function

    return game


def getFunctionForLine(words, game):
    if len(words) >= 2 and validateWordSequence(words[0:2], [s_intro_game, r_gameNum]):
        return None
    if len(words) >= 3 and validateWordSequence(words[0:3], [s_turn, r_number, s_hyphen]):
        return parseTurnLine
    if len(words) >= 3 and validateWordSequence(words[0:3], [r_playerLetter, s_intro_starts, s_intro_with]):
        return parseDeckStartLine
    if len(words) >= 4 and validateWordSequence(words[0:4], [r_playerLetter, s_buys, s_and, s_gains]):
        return parseBuyLine
    if len(words) >= 2 and validateWordSequence(words[0:2], [r_playerLetter, s_gains]):
        return parseGainLine
    if len(words) >= 2 and validateWordSequence(words[0:2], [r_playerLetter, s_trashes]):
        return parseTrashLine
    if len(words) >= 2 and validateWordSequence(words[0:2], [r_playerLetter, s_receives]):
        return parseReceivesLine
    if len(words) >= 2 and validateWordSequence(words[0:2], [r_playerLetter, s_returns]):
        return parseReturnsLine
    if len(words) >= 2 and validateWordSequence(words[0:2], [r_playerLetter, s_exiles]):
        return parseExileLine
    if len(words) >= 4 and validateWordSequence(words[0:2], [r_playerLetter, s_discards])\
            and validateWordSequence(words[-2:], [s_from, s_Exile]):
        return parseDiscardFromExileLine
    if len(words) >= 6 and validateWordSequence(words[0:2], [r_playerLetter, s_sets]):
        return parseSetsLine
    if len(words) >= 2 and validateWordSequence(words[0:2], [r_playerLetter, s_puts]):
        return parsePutsLine
    else:
        return None


def parseDeckStartLine(words, game):
    if game.getPlayerByInitial(words[0]) is None:
        player = Player()
        player.initial = words[0]
        game.players.append(player)
    game.getPlayerByInitial(
        words[0]).totalDeckCardNames += (parseMultipleCardsFromStrings(words, 3))


def parseTurnLine(words, game):
    if words[1] == '1':
        game.getPlayerByInitial(words[3][0]).name = ' '.join(words[3:])


def parseBuyLine(words, game):
    game.getPlayerByInitial(
        words[0]).totalDeckCardNames += parseMultipleCardsFromStrings(words, 4)


# "from trash", "onto their draw pile"
def parseGainLine(words, game):
    game.getPlayerByInitial(
        words[0]).totalDeckCardNames += parseMultipleCardsFromStrings(words, 2, stopWords=[s_from, s_onto])


def parseTrashLine(words, game):
    removeItemsFromList(game.getPlayerByInitial(
        words[0]).totalDeckCardNames, parseMultipleCardsFromStrings(words, 2))


def parseExileLine(words, game):
    removeItemsFromList(game.getPlayerByInitial(
        words[0]).totalDeckCardNames, parseMultipleCardsFromStrings(words, 2))


def parseDiscardFromExileLine(words, game):
    game.getPlayerByInitial(
        words[0]).totalDeckCardNames += parseMultipleCardsFromStrings(words, 2, stopWords=[s_from])


# "to the Horse pile", "-Coin token ..."
def parseReturnsLine(words, game):
    removeItemsFromList(game.getPlayerByInitial(
        words[0]).totalDeckCardNames, parseMultipleCardsFromStrings(words, 2, stopWords=[s_to, s_minus_Coin]))


def parseReceivesLine(words, game):
    game.getPlayerByInitial(
        words[0]).totalDeckCardNames += parseMultipleCardsFromStrings(words, 2)


# "aside with Native Village"
# "a card aside with Library"
# "Druid sets {Boon} aside."
# "sets 2 Coppers aside."
def parseSetsLine(words, game):
    if words[0] == s_Druid or validateWordSequence(words[-1:], [s_aside]):
        return
    removeItemsFromList(game.getPlayerByInitial(
        words[0]).totalDeckCardNames, parseMultipleCardsFromStrings(words, 2, stopWords=[s_aside, s_card]))


# "into their hand"
# "on their Island mad"
# "puts a Gold in hand (Crypt)."
# "puts a Magpie back onto their deck."
def parsePutsLine(words, game):
    if validateWordSequence(words[-3:], [s_into, s_their, s_hand])\
            or validateWordSequence(words[-1:], [s_CryptBrackets])\
            or validateWordSequence(words[-2:], [s_CargoLeftBracket, s_ShipRightBracket])\
            or validateWordSequence(words[-4:], [s_back, s_onto, s_their, s_deck]):
        return
    removeItemsFromList(game.getPlayerByInitial(
        words[0]).totalDeckCardNames, parseMultipleCardsFromStrings(words, 2, stopWords=[s_on]))

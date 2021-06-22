from enum import Enum

from logAnalyzer.logParser.strings import *  # all prefixed with s_ or r_
from logAnalyzer.logParser.cardNameFilter import getFilteredCardName
from logAnalyzer.game import Game, Player
from logAnalyzer.utils.logger import logError
from logAnalyzer.utils.pythonUtils import removeItemsFromList

# Takes in 2 lists of words (str/regexp) and returns T/F if matching
# Works on both strings and regexps


def validateWordSequence(testWords, referenceWords):
    for wordIndex in range(len(testWords)):
        if callable(getattr(referenceWords[wordIndex], 'match', None)):
            # Regular Experession
            if not referenceWords[wordIndex].match(testWords[wordIndex]):
                logError('Parse Error: ' + testWords[wordIndex] +
                         'not equal to ' + referenceWords[wordIndex].pattern)
                return False
        else:
            # String
            if testWords[wordIndex] != referenceWords[wordIndex]:
                logError('Parse Error: ' + testWords[wordIndex] +
                         'not equal to ' + referenceWords[wordIndex])
                return False
    return len(testWords) == len(referenceWords)


def cardNamesFromLogStrings(words, firstWordIndex):
    words = words[firstWordIndex:]
    listToReturn = []
    "J draws 2 Coppers, a Silver, an Estate and a Groom."
    i = 0
    while i < len(words):
        if words[i] == s_and:
            i += 1
        qtyString = words[i]
        if r_number.match(qtyString):
            cardQuantity = int(qtyString)
        elif qtyString == s_a or qtyString == s_an:
            cardQuantity = 1
        i += 1  # processed qty
        nameString = words[i]
        # loop, adding words until we know we can't
        while(True):
            if i == (len(words)-1) or (getFilteredCardName(nameString) is not None and getFilteredCardName(nameString + ' ' + words[i+1]) is None):
                break
            nameString = nameString + ' ' + words[i+1]
            i += 1
        if nameString[-1] == '.' or nameString[-1] == ',':
            nameString = nameString[0:-1]
        listToReturn += ([getFilteredCardName(nameString)] * cardQuantity)
        i += 1
    return listToReturn

# The initial parse , used for gathering # of players and their initials
# Not using getFunctionForLine approach, since this parse is so janky (yet short).
# Returns a GameState with:
# - players with names and initials, but empty decks.
# Needs to construct the gameState itself since GameState init needs to know # of players to construct them


def playerNamesParse(logString, game):
    lines = logString.split('\n')

    for line in lines:
        words = line.split()
        if len(words) >= 3 and validateWordSequence(words[1:3], [s_intro_starts, s_intro_With]):
            if game.getPlayerByInitial(words[0]) is None:
                player = Player()
                player.initial = words[0]
                game.players.append(player)
        if len(words) >= 3 and validateWordSequence(words[0:3], [s_turn, '1', s_hyphen]):
            player = game.getPlayerByInitial(
                words[3][0])  # first letter of name
            if player is None:
                assert False
            player.name = ' '.join(words[3:])


def logToGame(logString):

    game = Game()

    playerNamesParse(logString, game)

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
    if len(words) >= 2 and validateWordSequence(words[0:2], [r_playerLetter, s_intro_starts]):
        return parseDeckStartLine
    if len(words) >= 4 and validateWordSequence(words[0:4], [r_playerLetter, s_buys, s_and, s_gains]):
        return parseBuyLine
    if len(words) >= 2 and validateWordSequence(words[0:2], [r_playerLetter, s_gains]):
        return parseGainLine
    if len(words) >= 2 and validateWordSequence(words[0:2], [r_playerLetter, s_trashes]):
        return parseTrashLine
    else:
        return None


def parseDeckStartLine(words, game):
    playerInitial = words[0]
    game.getPlayerByInitial(
        playerInitial).cardNames += (cardNamesFromLogStrings(words, 3))


def parseTurnLine(words, game):
    None
    # game.incrementTurn() # this existed on gGames.


def parseBuyLine(words, game):
    game.getPlayerByInitial(
        words[0]).cardNames += cardNamesFromLogStrings(words, 4)


def parseGainLine(words, game):
    game.getPlayerByInitial(
        words[0]).cardNames += cardNamesFromLogStrings(words, 2)


def parseTrashLine(words, game):
    removeItemsFromList(game.getPlayerByInitial(
        words[0]).cardNames, cardNamesFromLogStrings(words, 2))

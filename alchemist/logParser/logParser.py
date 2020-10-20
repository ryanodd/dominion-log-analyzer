from enum import Enum

from utils.dominionOnlineLogParser.strings import * # all prefixed with s_ or r_
from utils.dominionOnlineLogParser.cardNames import getCardByName
from game.gameState import GameState
from game.playerState import PlayerState
from utils.log import log, logError
from utils.cardUtils import removeCardsFromListByNames

# Takes in 2 lists of words (str/regexp) and returns T/F if matching
# Works on both strings and regexps
def validateWordSequence(testWords, referenceWords):
  for wordIndex in range(len(testWords)):
    if callable(getattr(referenceWords[wordIndex], 'match', None)):
      # Regular Experession
      if not referenceWords[wordIndex].match(testWords[wordIndex]):
        log('Parse Error: ' + testWords[wordIndex] + 'not equal to ' + referenceWords[wordIndex].pattern)
        return False
    else:
      # String
      if testWords[wordIndex] != referenceWords[wordIndex]:
        log('Parse Error: ' + testWords[wordIndex] + 'not equal to ' + referenceWords[wordIndex])
        return False
  return len(testWords) == len(referenceWords)

def cardsFromLogStrings(words, firstWordIndex, shouldReturnNames=False):
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
    i += 1 # processed qty
    nameString = words[i]
    # loop, adding words until we know we can't
    while(True):
      if i == (len(words)-1) or (getCardByName(nameString) is not None and getCardByName(nameString + ' ' + words[i+1]) is None):
        break
      nameString = nameString + ' ' + words[i+1]
      i += 1
    if nameString[-1] == '.' or nameString[-1] == ',':
      nameString = nameString[0:-1]
    card = getCardByName(nameString)
    if shouldReturnNames:
      listToReturn += [card.name] * cardQuantity
    else:
      listToReturn += [card] * cardQuantity
    i += 1
  return listToReturn

# The initial parse , used for gathering # of players and their initials
# Not using getFunctionForLine approach, since this parse is so janky (yet short).
# Returns a GameState with:
# - players with names and initials, but empty decks.
# Needs to construct the gameState itself since GameState init needs to know # of players to construct them
def playerNamesParse(logString):
  lines = logString.split('\n')
  players = []

  for line in lines:
    words = line.split()
    if len(words) >= 2 and validateWordSequence(words[0:3], [s_turn, '1', s_hyphen]):
      players.append(PlayerState(' '.join(words[3:]), []))
      players[-1].initial = players[-1].name[0]
      # TODO: error-checking for players having the same initials (lots of work to get around)
  
  return GameState([], players)

def logToGameState(logString):

  game = playerNamesParse(logString)

  lines = logString.split('\n')
  for line in lines:
    words = line.split()
    functionToCall = getFunctionForLine(words, game)
    if functionToCall is not None:
      functionToCall(words, game) # get & execute function

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
  game.playerByInitial(playerInitial).deck += (cardsFromLogStrings(words, 3))

def parseTurnLine(words, game):
  game.incrementTurn()

def parseBuyLine(words, game):
  game.playerByInitial(words[0]).deck += cardsFromLogStrings(words, 4)

def parseGainLine(words, game):
  game.playerByInitial(words[0]).deck += cardsFromLogStrings(words, 2)

def parseTrashLine(words, game):
  removeCardsFromListByNames(game.playerByInitial(words[0]).deck, cardsFromLogStrings(words, 2, True))
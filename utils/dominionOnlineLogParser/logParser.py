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

def cardsFromLogStrings(line, firstWordIndex, shouldReturnNames=False):
  words = line.split(' ')[firstWordIndex:]
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

# Global Data, careful
playersByInitial = {}

def logToGameState(logString):
  # Reset Global Data
  global playersByInitial
  playersByInitial = {}  

  NUM_PLAYERS = 2 # TODO: could probably find this from first few lines
  players = []
  for _ in range(NUM_PLAYERS):
      players.append(PlayerState('bob', []))
  game = GameState([], players)
  lines = logString.split('\n')

  for line in lines:
      functionToCall = getFunctionForLine(line, game)
      if functionToCall is not None:
        functionToCall(line, game) # get & execute function

  return game

def getFunctionForLine(line, game):
  words = line.split(' ')
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

def parseDeckStartLine(line, game):
  words = line.split(' ')
  playerInitial = words[0]
  if playerInitial not in playersByInitial: # Add this player to our initials map
    playersByInitial[playerInitial] = game.players[len(playersByInitial)]
  playersByInitial[playerInitial].deck += (cardsFromLogStrings(line, 3))

def parseTurnLine(line, game):
  words = line.split(' ')
  roundNum = words[1]
  game.incrementTurn()

def parseBuyLine(line, game):
  words = line.split(' ')
  playersByInitial[words[0]].deck += cardsFromLogStrings(line, 4)

def parseGainLine(line, game):
  words = line.split(' ')
  playersByInitial[words[0]].deck += cardsFromLogStrings(line, 2)

def parseTrashLine(line, game):
  words = line.split(' ')
  removeCardsFromListByNames(playersByInitial[words[0]].deck, cardsFromLogStrings(line, 2, True))
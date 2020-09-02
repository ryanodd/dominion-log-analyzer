from enum import Enum
from game.gameState import GameState
from utils.log import log, logError
from utils.dominionOnlineLogParser.strings import * # all prefixed with s_ or r_

# Works on both strings and regexps
def validateWordSequence(testWords, referenceWords):
  for wordIndex in range(len(testWords)):
    if callable(getattr(referenceWords[wordIndex], 'match', None)):
      # Regular Experession
      if not referenceWords[wordIndex].match(testWords[wordIndex]):
        log('Parse Error: ' + testWords[wordIndex] + 'not equal to ' + referenceWords[wordIndex])
        return False
    else:
      # String
      if testWords[wordIndex] != referenceWords[wordIndex]:
        log('Parse Error: ' + testWords[wordIndex] + 'not equal to ' + referenceWords[wordIndex])
        return False
  return len(testWords) == len(referenceWords)

def cardsFromLogStrings(line, firstWordIndex):
  words = line.split(' ')[firstWordIndex:-1]
  cardsToReturn = []
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
    if nameString[-1] == '.' or nameString[-1] == ',':
      nameString = nameString[0:-2]
    card = getCardByName(nameString)
    cardsToReturn += [card] * cardQuantity
    i += 1
  return cardsToReturn

playersByInitial = {}

def logToGameState(logString):
  game = GameState()
  lines = logString.split('\n')

  for line in lines:
      getFunctionForLine(line, game)(line, game) # get & execute function

def getFunctionForLine(line, game):
  words = line.split(' ')
  if validateWordSequence(words[0-1], [s_intro_game, r_gameNum]):
    return None
  if validateWordSequence(words[0-2], [s_turn, r_number, s_hyphen]):
    return parseTurnLine
  if validateWordSequence(words[0-1], [r_playerLetter, s_intro_starts]):
    return parseDeckStartLine
  if validateWordSequence(words[0-3], [r_playerLetter, s_buys, s_and, s_gains]):
    return parseBuyLine
  if validateWordSequence(words[0-1], [r_playerLetter, s_gains]):
    return parseGainLine

def parseDeckStartLine(line, game):
  words = line.split(' ')
  playerInitial = words[0]
  if playerInitial not in playerInitials: # Add this player to our initials map
    playerInitials[playerInitial] = game.players[len(playersByInitial)]
  playersByInitial[playerInitial].deck.append(cardsFromLogString(line, 3))

def parseTurnLine(line, game):
  words = line.split(' ')
  roundNum = words[1]
  if roundNum == 1: # Populate names
    if game.players[0].name != '': # "if this isn't the first Turn line" might want a better way to check this
      game.incrementTurn()
    game.players[game.currentPlayerIndex] = "a" # TODO string maneuver
  else:
    game.incrementTurn()
    assert game.players[game.currentPlayerIndex].name == "a" # TODO string maneuver

def parseBuyLine(line, game):
  words = line.split(' ')
  playersByInitial[words[0]].deck += cardsFromLogStrings(line, 4)

def parseGainLine(line, game):
  words = line.split(' ')
  playersByInitial[words[0]].deck += cardsFromLogStrings(line, 2)
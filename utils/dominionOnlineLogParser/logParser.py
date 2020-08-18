import re
from enum import Enum
from utils.log import log, logError

r_capitalizedWord = re.compile
r_number = re.compile('[0-9]+')
r_endsWithPeriod = re.compile('[^ ]*\.')

r_playerLetter = re.compile('[A-Z]')
r_gameNum = re.compile('\#[0-9]*')
r_moneyIndicator = re.compile('\(\+\$[0-9]+\)')

s_intro_game = 'Game'
s_intro_unrated = 'unrated'
s_intro_starts = 'starts'
s_intro_With = 'with'

s_turn = 'Turn'

s_draws = 'draws'
s_shuffles = 'shuffles'
s_plays = 'plays'
s_buys = 'buys'
s_gains = 'gains'

s_card = 'card'
s_cards = 'cards'
s_deck = 'deck'

s_their = 'their'
s_and = 'and'
s_a = 'a'
s_an = 'an'

s_END = 'Players'


log = "\
Game #52848131, unrated.\
\
L starts with 7 Coppers.\
L starts with 3 Estates.\
J starts with 7 Coppers.\
J starts with 3 Estates.\
L shuffles their deck.\
L draws 5 cards.\
J shuffles their deck.\
J draws 3 Coppers and 2 Estates.\
\
Turn 1 - Lord Rattington\
L plays 3 Coppers. (+$3)\
L buys and gains a Silver.\
L draws 5 cards.\
\
Turn 1 - Jazzercise\
J plays 3 Coppers. (+$3)\
J buys and gains a Silver.\
J draws 4 Coppers and an Estate.\
\
Turn 2 - Lord Rattington\
L plays 4 Coppers. (+$4)\
L buys and gains an Oracle.\
L shuffles their deck.\
L draws 5 cards.\
\
Turn 2 - Jazzercise\
J plays 4 Coppers. (+$4)\
J buys and gains a Groom.\
J shuffles their deck.\
J draws 2 Coppers, a Silver, an Estate and a Groom.\
\
Turn 3 - Lord Rattington\
L plays an Oracle.\
L reveals 2 Estates.\
L discards 2 Estates.\
J reveals 2 Coppers.\
J discards 2 Coppers.\
L draws 2 cards.\
L plays 5 Coppers. (+$5)\
L buys and gains a Patrol.\
L shuffles their deck.\
L draws 5 cards.\
\
Turn 3 - Jazzercise\
\
Players can see spectator chat\
Joining game #52848131 on tokyo.\
message\
"

ignore = []


class State(Enum):
  UNKNOWN = 0
  ERROR = 1
  FINISHED = 2
  EXPECTING_GAMEINFO_LINE = 3
  EXPECTING_TURNSTART_LINE = 4
  PLAYER_LETTER_FOUND = 5
  PLAYER_VERB_FOUND = 6

def validateWordSequence(testWords, referenceWords):
  for wordIndex in range(len(testWords)):
    if callable(getattr(referenceWords[wordIndex], 'match', None)):
      # Matched Regular Experession
      if not referenceWords[wordIndex].match(testWords[wordIndex]):
        log('Parse Error: ' + testWords[wordIndex] + 'not equal to ' + referenceWords[wordIndex])
        return False
    else:
      if testWords[wordIndex] != referenceWords[wordIndex]:
        log('Parse Error: ' + testWords[wordIndex] + 'not equal to ' + referenceWords[wordIndex])
        return False
  return len(testWords) == len(referenceWords)

def validateAndPopTopWordsOfStack(referenceWords, stack):
  if len(stack) < len(referenceWords):
    logError('validateAndPopTopWordsOfStack Error: stack not big enough for testWords')
  stackToVerify = []
  for referenceWord in referenceWords:
    stackToVerify.append(stack.pop())
  return validateWordSequence(stackToVerify, referenceWords)


def logToGameState(logString):
  state = State.UNKNOWN
  lines = logString.split('\n').reverse()
  currentLine = lines[-1]
  while state != State.FINISHED and state != State.ERROR:
    if state == State.UNKNOWN:
      # TODO: Adapt to missing top of log
      state = State.EXPECTING_GAMEINFO_LINE
    elif state == State.EXPECTING_GAMEINFO_LINE:
      words = currentLine.pop().split(' ').reverse()
      if validateAndPopTopWordsOfStack([s_intro_game, r_gameNum, s_intro_unrated], words):
        #Skip 2 line
        currentLine = lines.pop().pop()[-1] # pop pop!
    elif state == State.EXPECTING_TURNSTART_LINE:
      words = currentLine.pop().split(' ').reverse()
      if validateAndPopTopWordsOfStack([s_turn, r_number], words):
        # Skip 1 line
        currentLine = lines.pop()[-1]
      else:
        logError("Parse Error: Expected turn start sequence")


  while words:
    word = words[-1]





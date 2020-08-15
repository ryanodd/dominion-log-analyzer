from enum import Enum

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

def parseLog(logString):
  class State(Enum):
    LINE_START = 1
    PLAYER_LETTER_FOUND = 2
    PLAYER_VERB_FOUND = 3
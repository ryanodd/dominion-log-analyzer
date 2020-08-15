from enum import Enum
from game.card.card import CardType

class ChoiceID(Enum):
    ACTION = 1
    TREASURE = 2
    BUY = 3

    ARTISAN1 = 4
    ARTISAN2 = 5
    BANDIT = 6
    BUREAUCRAT = 7
    CELLAR = 8
    CHAPEL = 9
    HARBINGER = 10
    LIBRARY = 11
    MILITIA = 12
    MINE1 = 13
    MINE2 = 14
    MONEYLENDER = 15
    POACHER = 16
    REMODEL1 = 17
    REMODEL2 = 18
    SENTRY1 = 19
    SENTRY2 = 20
    SENTRY3 = 21
    THRONEROOM = 22
    VASSAL = 23
    WORKSHOP = 24

verifiers = {}


def verify_action(game, response):
    return CardType.ACTION in game.currentPlayer.hand[response].types
verifiers[ChoiceID.ACTION] = verify_action

def verify_treasure(game, response):
    return CardType.TREASURE in game.currentPlayer.hand[response].types
verifiers[ChoiceID.TREASURE] = verify_treasure

def verify_buy(game, response):
    return game.currentPlayer.action in game.currentPlayer.hand[response].types
verifiers[ChoiceID.BUY] = verify_buy

#------------



#------------

def getVerifier(choiceID):
  if choiceID in verifiers:
    return verifiers[choiceID]
  else:
    return None
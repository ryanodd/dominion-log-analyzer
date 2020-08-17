from enum import Enum
from game.card.card import CardType
from game.choice import ChoiceID
from bot.cardInfo import getCardInfo
from bot.choose.chooseAction import chooseAction
from bot.choose.chooseTreasure import chooseTreasure
from bot.choose.chooseBuy import chooseBuy

choosers = {}

choosers[ChoiceID.ACTION] = chooseAction # Imported
choosers[ChoiceID.TREASURE] = chooseTreasure # Imported
choosers[ChoiceID.BUY] = chooseBuy # Imported

#------------

    # ARTISAN2 = 5
    # BANDIT = 6
    # BUREAUCRAT = 7
    # CELLAR = 8
    # CHAPEL = 9
    # HARBINGER = 10
    # LIBRARY = 11
    # MILITIA = 12
    # MINE1 = 13
    # MINE2 = 14
    # MONEYLENDER = 15
    # POACHER = 16
    # REMODEL1 = 17
    # REMODEL2 = 18
    # SENTRY1 = 19
    # SENTRY2 = 20
    # SENTRY3 = 21
    # THRONEROOM = 22
    # VASSAL = 23
    # WORKSHOP = 24
#------------

def getChooser(choiceID):
  if choiceID in choosers:
    return choosers[choiceID]
  else:
    return None
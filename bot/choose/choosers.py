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

# Brain blast theor: weigh between:
# 1. thing you want to do with it this turn
# 2. The thing you would do otherwise
# Opportunity cost compare??

# TODO: use cardInfo something like 'isBeneficialToHaveInHandThisTurn' calculatable.
# For now, this could discard Distant Lands over Estate
def chooseBureaucrat(choice, gameState, choosingPlayerIndex):
  player = gameState.players[choosingPlayerIndex]
  for handIndex in range(len(player.hand)):
    if CardType.VICTORY in player.hand[handIndex].types:
      return handIndex
choosers[ChoiceID.BUREAUCRAT] = chooseBureaucrat


    # ARTISAN1
    # ARTISAN2
    # BANDIT
      # BUREAUCRAT
    # CELLAR
    # CHAPEL
    # HARBINGER
    # LIBRARY
    # MILITIA
    # MINE1
    # MINE2
    # MONEYLENDER
    # POACHER
    # REMODEL1
    # REMODEL2
    # SENTRY1
    # SENTRY2
    # SENTRY3
    # THRONEROOM
    # VASSAL
    # WORKSHOP
#------------

def getChooser(choiceID):
  if choiceID in choosers:
    return choosers[choiceID]
  else:
    return None
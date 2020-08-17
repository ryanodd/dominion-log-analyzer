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

# Brain blast theory: weigh between:
# 1. thing you want to do with it this turn
# 2. The thing you would do otherwise
# Opportunity cost compare??

# TODO: use cardInfo something like 'isBeneficialToHaveInHandThisTurn' calculatable.
# For now, this could discard Distant Lands over Estate
def chooseBureaucratByIsVictory(choice, gameState, choosingPlayerIndex):
  player = gameState.players[choosingPlayerIndex]
  for handIndex in range(len(player.hand)):
    if CardType.VICTORY in player.hand[handIndex].types:
      return handIndex
choosers[ChoiceID.BUREAUCRAT] = chooseBureaucratByIsVictory

# Silvers, then Coppers, then by lowest cost treasure
# TODO obviously weigh these options better. Gold -> Platinum also
def chooseMineOneByLowestCost(choice, gameState, choosingPlayerIndex):
  player = gameState.players[choosingPlayerIndex]
  for handIndex in range(len(player.hand)):
    if  player.hand[handIndex].name == 'Silver':
      return handIndex
  for handIndex in range(len(player.hand)):
    if  player.hand[handIndex].name == 'Copper':
      return handIndex
  minCost = 0
  bestCardIndex = None
  for handIndex in range(len(player.hand)):
    card = player.hand[handIndex]
    if CardType.TREASURE in card.types and card.cost > minCost:
      minCost = card.cost
      bestCardIndex = handIndex
  return bestCardIndex
choosers[ChoiceID.MINE1] = chooseMineOneByLowestCost

def chooseMineTwoByHighestCost(choice, gameState, choosingPlayerIndex):

  # Possibly referencing the listing map wrong here?
  for listing in gameState.shop.listings:
    if listing.quantity >= 1 and CardType.TREASURE in listing.card.types and listing.card.cost > maxCost:
      maxCost = listing.card.cost
      bestCardName = listing.card.name
  return bestCardName
choosers[ChoiceID.MINE2] = chooseMineTwoByHighestCost

def chooseMoneylenderByIsCopper(choice, gameState, choosingPlayerIndex):
  player = gameState.players[choosingPlayerIndex]
  for handIndex in range(len(player.hand)):
    if player.hand[handIndex].name == 'Copper':
      return handIndex
  return None
choosers[ChoiceID.MONEYLENDER] = chooseMoneylenderByIsCopper

# TODO: this just references the top of the discard, not guaranteed to be it. Eventually each card needs a reference??
def chooseVassalByBeneficial(choice, gameState, choosingPlayerIndex):
  cardInQuestion = gameState.players[choosingPlayerIndex].discard[-1]
  return getCardInfo(cardInQuestion.name).beneficial
choosers[ChoiceID.VASSAL] = chooseVassalByBeneficial

    # ARTISAN1
    # ARTISAN2
    # BANDIT
      # BUREAUCRAT
    # CELLAR
    # CHAPEL
    # HARBINGER
    # LIBRARY
    # MILITIA - generic discard choice
      # MINE1
      # MINE2
      # MONEYLENDER
    # POACHER - generic discard choice
    # REMODEL1
    # REMODEL2 - generic gain choice
    # SENTRY1  - generic trash choice?
    # SENTRY2
    # SENTRY3
    # THRONEROOM - isBeneficial spectrum?
      # VASSAL
    # WORKSHOP - generic gain choice
#------------

def getChooser(choiceID):
  if choiceID in choosers:
    return choosers[choiceID]
  else:
    return None
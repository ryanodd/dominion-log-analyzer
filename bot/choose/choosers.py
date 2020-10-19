from enum import Enum
from game.card.gCard import CardType
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

# weigh between:
# - thing you want to do with it this turn
# - The things you would do otherwise
# Opportunity cost compare?

def chooseBanditByHighestMoney(choice, gameState, choosingPlayerIndex):
  maxCost = 0
  bestCardIndex = None
  for cardIndex in range(len(gameState.cardStoreStack[-1])):
    card = gameState.cardStoreStack[-1][cardIndex]
    if CardType.TREASURE in card.types and card.cost > maxCost:
      maxCost = card.cost
      bestCardIndex = cardIndex
  return bestCardIndex
choosers[ChoiceID.BANDIT] = chooseBanditByHighestMoney

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
    if CardType.TREASURE in card.types and card.cost < minCost:
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

  # LT = Long Term
  # ST = Short Term

    # ARTISAN1 - gain to hand LT + ST value compare
    # ARTISAN2 - topdeck: ST + 1 (with extra ST next turn)
        # BANDIT - trash opponent treasure: reasonable hardcode (for now)
        # BUREAUCRAT - topdeck victory: reasonable hardcode (for now)
      # CELLAR - compare discarded vs potential draw: ST
    # CHAPEL - ST + LT
      # HARBINGER - ST (+1?)
      # LIBRARY - ST (could be hardcodeed)
      # MILITIA - generic discard choice: ST
        # MINE1
        # MINE2
        # MONEYLENDER
      # POACHER - absolute ST
    # REMODEL1 - trash, with gain cost in mind: LT
    # REMODEL2 - gain: LT
    # SENTRY1  - trash: LT + ST (of drawing it)
      # SENTRY2 - discard: ST + 1 probably
      # SENTRY3 - order: ST, could probably be hardcoded well-
    # THRONEROOM - isBeneficial spectrum? ST or LT, whetever youre cloning
        # VASSAL
    # WORKSHOP - gain: LT
#------------

def getChooser(choiceID):
  if choiceID in choosers:
    return choosers[choiceID]
  else:
    return None
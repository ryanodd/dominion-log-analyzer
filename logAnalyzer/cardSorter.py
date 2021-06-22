from operator import attrgetter

def sortCardsByTypeThenCost(cards):
  s = sorted(cards, key=attrgetter('cost.value'))     # sort on secondary key
  victoryCards = []
  curseCards = []
  treasureCards = []
  actionCards = []
  otherCards = []
  for card in s:
    if card.isAction.value:
      actionCards.append(card)
    elif card.isVictory.value:
      victoryCards.append(card)
    elif card.isCurse.value:
      curseCards.append(card)
    elif card.isTreasure.value:
      treasureCards.append(card)
    else:
      otherCards.append(card)
  return victoryCards + curseCards + treasureCards + actionCards + otherCards

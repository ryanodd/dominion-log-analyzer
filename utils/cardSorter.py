from operator import attrgetter

from game.card.gCard import CardType

def sortCardsByTypeThenCost(cards):
  s = sorted(cards, key=attrgetter('cost'))     # sort on secondary key
  victoryCards = []
  curseCards = []
  treasureCards = []
  actionCards = []
  otherCards = []
  for card in s:
    if CardType.ACTION in card.types:
      actionCards.append(card)
    elif CardType.VICTORY in card.types:
      victoryCards.append(card)
    elif CardType.CURSE in card.types:
      curseCards.append(card)
    elif CardType.TREASURE in card.types:
      treasureCards.append(card)
    else:
      otherCards.append(card)
  return victoryCards + curseCards + treasureCards + actionCards + otherCards

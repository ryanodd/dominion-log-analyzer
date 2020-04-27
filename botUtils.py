import copy
from card import *

class CardInfo:
    def __init__(self, money=0, draws=0, actions=0, buys=0, vp=0):
        self.money = money
        self.draws = draws
        self.actions = actions
        self.buys = buys
        self.vp = vp

# Maps card names to CardInfo objects
info = {}

info['Estate'] = CardInfo(vp=1)
info['Duchy'] = CardInfo(vp=3)
info['Province'] = CardInfo(vp=6)
info['Curse'] = CardInfo(vp=-1)
info['Copper'] = CardInfo(money=1)
info['Silver'] = CardInfo(money=2)
info['Gold'] = CardInfo(money=3)


info['Festival'] = CardInfo(money=2, buys=1)
info['Gardens'] = CardInfo(vp=3) # wrong for now. Where should the math be done?
info['Laboratory'] = CardInfo(draws=2, actions=1)
info['Market'] = CardInfo(money=1, draws=1, actions=1, buys=1)
info['Smithy'] = CardInfo(draws=3)
info['Village'] = CardInfo(draws=1, actions=2)


def cardInfoByName(name):
    return info[name]

def cardCountByName(cards, name):
    count = 0
    for card in cards:
        if (card.name == name):
            count += 1
    return count

def terminalCount(cards):
    count = 0
    for card in cards:
        if (CardType.ACTION in card.types and info[card.name].actions == 0):
            count += 1
    return count

def isCardTerminal(card):
    if (CardType.ACTION not in card.types): return False
    return info[card.name].actions <= 0

# I don't like this formula
def deckValue(deck):
    deckSize = len(deck)
    totalMoney = 0.0
    totalDraws = 0.0
    for card in deck:
        totalMoney += info[card.name].money
        totalDraws += info[card.name].draws
    return totalMoney / max(1, (deckSize - totalDraws))

def deckValueIncrease(deck, card):
    potentialDeck = copy.deepcopy(deck)
    potentialDeck.append(card)
    return deckValue(potentialDeck) - deckValue(deck)

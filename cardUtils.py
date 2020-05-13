from log import *
from card import *
from objectiveCardInfo import getCardInfo

# O(n^2) !!!!
# Returns a new deck list, does not modify input deck
def trimFromDeck(deck, inputNames):
    names = inputNames.copy()
    returnDeck = []
    for card in deck:
        if (card.name not in names):
            returnDeck.append(card)
        else:
            names.remove(card.name)
    return returnDeck


def cardCountByName(cards, name):
    count = 0
    for card in cards:
        if (card.name == name):
            count += 1
    return count

def cardCountByType(cards, type):
    count = 0
    for card in cards:
        if (type in card.types):
            count += 1
    return count

def totalMoney(cards):
    total  = 0
    for card in cards:
        total += getCardInfo(card.name).money
    return total

def terminalCount(cards):
    count = 0
    for card in cards:
        if (CardType.ACTION in card.types and getCardInfo(card.name).actions == 0):
            count += 1
    return count

def extraActionsCount(cards):
    count = 0
    for card in cards:
        if (CardType.ACTION in card.types and getCardInfo(card.name).actions >= 2):
            count += 1
    return count

def isCardTerminal(card):
    if (CardType.ACTION not in card.types): return False
    return getCardInfo(card.name).actions <= 0

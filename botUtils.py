from card import *
from botKnowledge import getCardInfo

def cardCountByName(cards, name):
    count = 0
    for card in cards:
        if (card.name == name):
            count += 1
    return count

def terminalCount(cards):
    count = 0
    for card in cards:
        if (CardType.ACTION in card.types and getCardInfo(card.name).actions == 0):
            count += 1
    return count

def isCardTerminal(card):
    if (CardType.ACTION not in card.types): return False
    return getCardInfo(card.name).actions <= 0

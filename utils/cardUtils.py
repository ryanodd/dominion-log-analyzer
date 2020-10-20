from utils.log import logError
from game.card.gCard import CardType
from alchemist.card import getCard

def removeCardsFromListByNames(cardList, nameList):
    for name in nameList:
        for i in range(len(cardList)):
            if cardList[i].name == name:
                cardList.pop(i)
                break

def totalDraws(cards):
    total = 0
    for card in cards:
        total += getCard(card.name).draws.value
    return total

def totalMoney(cards):
    total  = 0
    for card in cards:
        total += getCard(card.name).money.value
    return total

def terminalCount(cards):
    count = 0
    for card in cards:
        if (CardType.ACTION in card.types and getCard(card.name).actions.value == 0):
            count += 1
    return count

def extraActionCount(cards):
    count = 0
    for card in cards:
        if (CardType.ACTION in card.types and getCard(card.name).actions.value >= 2):
            count += (getCard(card.name).actions.value - 1)
    return count

def isCardTerminal(card):
    if (CardType.ACTION not in card.types): return False
    return getCard(card.name).actions.value == 0
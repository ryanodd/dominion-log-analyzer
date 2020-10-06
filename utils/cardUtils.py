from utils.log import logError
from game.card.card import CardType
from bot.cardInfo import getCardInfo

def removeCardsFromListByNames(cardList, nameList):
    for name in nameList:
        for i in range(len(cardList)):
            if cardList[i].name == name:
                cardList.pop(i)
                break


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

def totalDraws(cards):
    total = 0
    for card in cards:
        total += getCardInfo(card.name).draws.value
    return total

def totalMoney(cards):
    total  = 0
    for card in cards:
        total += getCardInfo(card.name).money.value
    return total

def terminalCount(cards):
    count = 0
    for card in cards:
        if (CardType.ACTION in card.types and getCardInfo(card.name).actions.value == 0):
            count += 1
    return count

def extraActionCount(cards):
    count = 0
    for card in cards:
        if (CardType.ACTION in card.types and getCardInfo(card.name).actions.value >= 2):
            count += (getCardInfo(card.name).actions.value - 1)
    return count

def isCardTerminal(card):
    if (CardType.ACTION not in card.types): return False
    return getCardInfo(card.name).actions.value == 0
from utils.log import logError
from game.card.card import CardType

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
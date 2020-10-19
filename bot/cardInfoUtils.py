from bot.cardInfo import getCard
from game.card.gCard import CardType

class CardsReport:
    def __init__(self, value, messages=[]):
        self.value = value
        self.messages = messages

def getCardsReport(cards, fieldName):
    valueSum = 0
    messages = []
    for card in cards:
        valueObj = getattr(getCard(card.name), fieldName)
        valueSum += valueObj.value
        if valueObj.message != '':
            messageToAdd = (card.name + ' = ' + str(valueObj.value) + ' ' + fieldName + ' (' + valueObj.message + ')')
            if messageToAdd not in messages:
                messages.append(messageToAdd)
    return CardsReport(valueSum, messages)

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
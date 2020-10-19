from bot.cardInfo import getCardInfo
from game.card.gCard import CardType

class CardInfoSumReport:
    def __init__(self, value, messages=[]):
        self.value = value
        self.messages = messages

def getCardInfoSumReport(cards, fieldName):
    valueSum = 0
    messages = []
    for card in cards:
        valueObj = getattr(getCardInfo(card.name), fieldName)
        valueSum += valueObj.value
        if valueObj.message != '':
            messageToAdd = (card.name + ' = ' + str(valueObj.value) + ' ' + fieldName + ' (' + valueObj.message + ')')
            if messageToAdd not in messages:
                messages.append(messageToAdd)
    return CardInfoSumReport(valueSum, messages)

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
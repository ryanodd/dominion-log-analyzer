from alchemist.card import getCard
from alchemist.deckReport.valueReport import ValueReport

def getValueSumReports(cards, fieldNames):
    values = []
    for fieldName in fieldNames:
        values.append(getValueSumReport(cards, fieldName))
    return values

def getValueSumReport(cards, fieldName):
    valueSum = 0
    messages = []
    for card in cards:
        valueObj = getattr(getCard(card.name), fieldName)
        valueSum += valueObj.value
        for message in valueObj.messages:
            messageToAdd = (card.name + ' = ' + str(valueObj.value) + ' ' + fieldName + ' (' + message + ')')
            if messageToAdd not in messages:
                messages.append(messageToAdd)
    return ValueReport(valueSum, messages)


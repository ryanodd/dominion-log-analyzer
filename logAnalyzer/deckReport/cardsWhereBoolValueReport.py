from logAnalyzer.card import getCard
from logAnalyzer.deckReport.valueReport import ValueReport

# list of reports (each with a list of cards) for each boolean field supplied


def getCardsWhereBoolReports(cards, fieldNames):
    values = []
    for fieldName in fieldNames:
        values.append(getCardsWhereBoolReport(cards, fieldName))
    return values


def getCardsWhereBoolReport(cards, fieldName):
    returnCardNames = []
    messages = []
    for card in cards:
        valueObj = getattr(getCard(card.name), fieldName)

        # If the supplied boolean value is true, add to return list
        if valueObj.value is not None and valueObj.value:
            returnCardNames.append(card.name)

        for message in valueObj.messages:
            messageToAdd = (card.name + ' = ' + str(valueObj.value) +
                            ' ' + fieldName + ' (' + message + ')')
            if messageToAdd not in messages:
                messages.append(messageToAdd)

    return ValueReport(returnCardNames, messages)

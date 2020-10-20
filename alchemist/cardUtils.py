from alchemist.card import getCard

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
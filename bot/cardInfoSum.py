from bot.cardInfo import getCardInfo

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
            messages.append(card.name + ' (counts as ' + str(valueObj.value) + ' ' + fieldName + '): ' + valueObj.message)
    return CardInfoSumReport(valueSum, messages)
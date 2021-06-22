from logAnalyzer.cards.cards import getCard
from logAnalyzer.deckReport.valueReport import ValueReport

# This is its own report fn (not valueSumReport) because this not a summable statistic


def getEffectiveMoneyDensityReport(cards):
    moneySum = 0
    drawsSum = 0
    messages = []
    # Sum over money & draws (needed to calculate EMD). Decided not to use valueSumReports here for now (things could change)
    for card in cards:
        moneyValue = getCard(card.name).money
        moneySum += moneyValue.value
        for message in moneyValue.messages:
            messageToAdd = (card.name + ' = ' +
                            str(moneyValue.value) + ' money (' + message + ')')
            if messageToAdd not in messages:
                messages.append(messageToAdd)
        drawsValue = getCard(card.name).draws
        drawsSum += drawsValue.value
        for message in drawsValue.messages:
            messageToAdd = (card.name + ' = ' +
                            str(drawsValue.value) + ' draws (' + message + ')')
            if messageToAdd not in messages:
                messages.append(messageToAdd)
    numCards = len(cards)
    effectiveStops = max(1, numCards - drawsSum)
    moneyDensity = moneySum / effectiveStops
    return ValueReport(moneyDensity, messages)

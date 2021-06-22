from logAnalyzer.cardSorter import sortCardsByTypeThenCost
from logAnalyzer.deckReport.valueSumReport import getValueSumReport
from logAnalyzer.deckReport.cardsWhereBoolValueReport import getCardsWhereBoolReport
from logAnalyzer.deckReport.effectiveMoneyDensityReport import getEffectiveMoneyDensityReport
from logAnalyzer.card import getCard
from logAnalyzer.deckReport.valueReport import ValueReport

def getDeckReport(player):
    cards = []
    for name in player.cardNames:
        cards.append(getCard(name))

    deckReport = {}
    deckReport['playerName'] = player.name
    deckReport['playerInitial'] = player.name[0]

    deckReport['cardNameList'] = []
    cards = sortCardsByTypeThenCost(cards)
    for card in cards:
        deckReport['cardNameList'].append(card.name)

    deckReport['cardListReports'] = {}
    fieldsToReport_Bool = [\
        'doesGain',\
        'doesTrash',\
        'isAttack'\
    ]
    for fieldName in fieldsToReport_Bool:
        deckReport['cardListReports'][fieldName] = getCardsWhereBoolReport(cards, fieldName).__dict__

    deckReport['card'] = ValueReport(len(player.cardNames), []).__dict__
    
    deckReport['numberReports'] = {}
    fieldsToReport_Sum = [\
        'money',\
        'stop',\
        'draws',\
        'extraDraws',\
        'actions',\
        'terminal',\
        'extraActions',\
        'buys',\
    ]

    deckReport['numberReports']['card'] = ValueReport(len(player.cardNames), []).__dict__
    for fieldName in fieldsToReport_Sum:
        deckReport['numberReports'][fieldName] = getValueSumReport(cards, fieldName).__dict__
    deckReport['numberReports']['effectiveMoneyDensity'] = getEffectiveMoneyDensityReport(cards).__dict__
    
    return deckReport

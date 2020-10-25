from alchemist.cardSorter import sortCardsByTypeThenCost
from alchemist.deckReport.valueSumReport import getValueSumReport
from alchemist.deckReport.cardsWhereBoolValueReport import getCardsWhereBoolReport
from alchemist.card import getCard
from alchemist.deckReport.valueReport import ValueReport

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

    fieldsToReport_Bool = [\
        'doesGain',\
        'doesTrash',\
        'isAttack'\
    ]
    for fieldName in fieldsToReport_Bool:
        deckReport[fieldName] = getValueSumReport(cards, fieldName).__dict__

    deckReport['card'] = ValueReport(len(player.cardNames), []).__dict__
    fieldsToReport_Sum = [\
        'money',\
        'stop',\
        'draws',\
        'extraDraws',\
        'actions',\
        'terminal',\
        'extraActions',\
        'buys'\
    ]
    # TODO: Money Density (Effective Money Density)
    for fieldName in fieldsToReport_Sum:
        deckReport[fieldName] = getValueSumReport(cards, fieldName).__dict__
    
    return deckReport
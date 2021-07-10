from logAnalyzer.cardSorter import sortCardsByTypeThenCost
from logAnalyzer.cards.cards import getCard


def getDeckListReport(player):
    cards = []
    for name in player.totalDeckCardNames:
        cards.append(getCard(name))

    deckReport = {}
    deckReport['playerName'] = player.name
    deckReport['playerInitial'] = player.name[0]

    deckReport['cardNameList'] = []
    cards = sortCardsByTypeThenCost(cards)
    for card in cards:
        deckReport['cardNameList'].append(card.name)

    return deckReport

# Data display
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from card import CardType
from game import *
from bigMoneyBot import BigMoneyBot
from objectiveCardInfo import getCardInfo
import cardFactory
from stringUtils import cardsFromDeckString

NUM_SAMPLES = 10000

class TurnSet:
    def __init__(self, name, bot, deck):
        self.name = name
        self.bot = bot
        self.deck = deck
        self.samples = []
    
        # May want to separate these into another class?
        self.averageMoney = 0
        self.averageActionsPlayed = 0
        self.averageActionsDiscarded = 0

turns = []

BMBot = BigMoneyBot({})

deckStrings = []
deckStrings.append("19 Copper, 9 Smithy, 2 Laboratory")

for deckString in deckStrings:
    turns.append(TurnSet(deckString, BMBot, cardsFromDeckString(deckString)))

# Run turns
for t in turns:
    for i in range(NUM_SAMPLES):
        b = Board([], 1)
        t.samples.append(Player(b, t.bot, t.deck.copy()))
        t.samples[-1].turn()
        

# Collect Stats
for t in turns:
    totalMoney = 0
    totalActionsPlayed = 0
    totalActionsDiscarded = 0
    for sample in t.samples:
        totalMoney += sample.log.turns[0].moneyAvailable

        totalActionsPlayed += len(sample.log.turns[0].actionsPlayed)

        cardsDiscarded = sample.log.turns[0].endingHand
        for card in cardsDiscarded:
            if (CardType.ACTION in card.types):
                totalActionsDiscarded += 1
    t.averageMoney = totalMoney / len(t.samples)
    t.averageActionsPlayed = totalActionsPlayed / len(t.samples)
    t.averageActionsDiscarded = totalActionsDiscarded / len(t.samples)

# Display Stats
for t in turns:
    if (t.averageActionsPlayed + t.averageActionsDiscarded == 0):
        actionPlayRate = -1
    else:
        actionPlayRate = t.averageActionsPlayed / (t.averageActionsPlayed + t.averageActionsDiscarded)
    print("%s: ATM(calcATM): %.2f(%.2f) actionRte: %.2f" % (t.name, t. averageMoney, t.bot.calcATM(t.deck), actionPlayRate))

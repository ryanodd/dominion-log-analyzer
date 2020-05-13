# Data display
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from card import CardType
from board import Board
from player import Player
from bigMoneyBot import Bot
from objectiveCardInfo import getCardInfo
import cardFactory
from stringUtils import cardsFromDeckString
import welfordAlg

NUM_SAMPLES = 2000

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

calcATMBot = Bot({"useCalcATM": True})

deckStrings = []
deckStrings.append("1 Copper, 10 Silver, 1 Gold")
deckStrings.append("6 Copper, 6 Gold")

for deckString in deckStrings:
    turns.append(TurnSet(deckString, calcATMBot, cardsFromDeckString(deckString)))

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
    t.moneyDist = [0, 0, 0]
    t.actionDist = [0, 0, 0]
    for sample in t.samples:
        moneyAvailable = sample.log.turns[0].moneyAvailable
        t.moneyDist = welfordAlg.update(t.moneyDist, moneyAvailable)

        totalActionsPlayed += len(sample.log.turns[0].actionsPlayed)
        t.actionDist = welfordAlg.update(t.actionDist, totalActionsPlayed)

        cardsDiscarded = sample.log.turns[0].endingHand
        for card in cardsDiscarded:
            if (CardType.ACTION in card.types):
                totalActionsDiscarded += 1
    t.averageActionsPlayed = totalActionsPlayed / len(t.samples)
    t.averageActionsDiscarded = totalActionsDiscarded / len(t.samples)

# Display Stats
for t in turns:
    if (t.averageActionsPlayed + t.averageActionsDiscarded == 0):
        actionPlayRate = -1
    else:
        actionPlayRate = t.averageActionsPlayed / (t.averageActionsPlayed + t.averageActionsDiscarded)
    print("%s: ATM(M2) %.2f(%.0f) calcATM: %.2f actionRte(M2): %.2f(%.0f)" % (t.name, t.moneyDist[1], t.moneyDist[2], t.bot.calcATM(t.deck), actionPlayRate, t.actionDist[2]))

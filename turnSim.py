# Data display
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from card import CardType
from board import Board
from player import Player
from bot import Bot
from objectiveCardInfo import getCardInfo
import cardFactory
import welfordAlg

class TurnSimInfo:
    def __init__(self, moneyDist, actionDist, averageActionsPlayed, averageActionsDiscarded):
        self.moneyDist = moneyDist
        self.actionDist = actionDist
        self.averageActionsPlayed = averageActionsPlayed
        self.averageActionsDiscarded = averageActionsDiscarded

def simDeckTurn(deck, numSamples):
    samples = []
    bot = Bot({"useCalcATM": False}) # Hardcoding the bot to avoid infinite recursion when the bot tries to use us

    # Run turns
    for i in range(numSamples):
        b = Board([], 1)
        samples.append(Player(b, bot, deck.copy()))
        samples[-1].turn()

    # Collect Stats
    totalActionsPlayed = 0
    totalActionsDiscarded = 0
    moneyDist = [0, 0, 0]
    actionDist = [0, 0, 0]
    for sample in samples:
        moneyAvailable = sample.log.turns[0].moneyAvailable
        moneyDist = welfordAlg.update(moneyDist, moneyAvailable)

        totalActionsPlayed += len(sample.log.turns[0].actionsPlayed)
        actionDist = welfordAlg.update(actionDist, totalActionsPlayed)

        cardsDiscarded = sample.log.turns[0].endingHand
        for card in cardsDiscarded:
            if (CardType.ACTION in card.types):
                totalActionsDiscarded += 1
    averageActionsPlayed = totalActionsPlayed / len(samples)
    averageActionsDiscarded = totalActionsDiscarded / len(samples)

    # Unused: actionDist, money M2, averageActions played/discarded
    return TurnSimInfo(moneyDist, actionDist, averageActionsPlayed, averageActionsDiscarded)

# Data display
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from game.card import CardType
from game.board import Board
from game.player import Player
from bot.bot import Bot
from bot.objectiveCardInfo import getCardInfo
from utils.welfordAlg import welfordUpdate, welfordFinalize

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
    for _ in range(numSamples):
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
        moneyDist = welfordUpdate(moneyDist, moneyAvailable)

        totalActionsPlayed += len(sample.log.turns[0].actionsPlayed)
        actionDist = welfordUpdate(actionDist, totalActionsPlayed)

        cardsDiscarded = sample.log.turns[0].endingHand
        for card in cardsDiscarded:
            if (CardType.ACTION in card.types):
                totalActionsDiscarded += 1
    moneyDist = welfordFinalize(moneyDist)
    actionDist = welfordFinalize(actionDist)
    averageActionsPlayed = totalActionsPlayed / len(samples)
    averageActionsDiscarded = totalActionsDiscarded / len(samples)

    return TurnSimInfo(moneyDist, actionDist, averageActionsPlayed, averageActionsDiscarded)
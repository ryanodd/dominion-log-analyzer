import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math

from utils.stringUtils import cardsFromDeckString
from sim.gameSim import simGame
from sim.turnSim import simDeckTurn
from bot.bot import Bot

class GameTestSet:
    def __init__(self, name, bots, shopCards):
        self.name = name
        self.bots = bots
        self.shopCards = shopCards

def gameTests():

    NUM_SAMPLES = 50

    mathBot = Bot({"calcATMMath": True})

    shopStrings = {}
    shopStrings['classic'] = "1 Smithy, 1 Market, 1 Village, 1 Festival"
    

    games = []
    games.append(GameTestSet("MathBot", [mathBot], cardsFromDeckString(shopStrings['classic'])))

    # Display Stats
    for g in games:
        res = simGame(g.bots, g.shopCards, NUM_SAMPLES)
        # print(g.name)
        # for i in range(30):
        #     if (i in g.roundDist):
        #         print("%s rounds: %s" % (i, g.roundDist[i]))
        # print()
        plotDataFrame = pd.DataFrame({"Rounds": list(res.roundDist.keys()), "Frequency": list(res.roundDist.values())})
        sns.lineplot(data=plotDataFrame, x="Rounds", y="Frequency", label=g.name), 
    plt.show()

def turnTests():
    NUM_SAMPLES = 4000

    calcATMReferenceBot = Bot({"useCalcATM": False})

    deckStrings = []
    #deckStrings.append("7 Copper, 3 Estate, 4 Silver, 2 Gold")
    deckStrings.append("7 Copper, 3 Estate, 3 Silver, 2 Smithy, 1 Gold")
    #deckStrings.append("7 Copper, 3 Estate, 3 Silver, 4 Smithy, 1 Gold")
    #deckStrings.append("7 Copper, 3 Estate, 3 Silver, 2 Smithy, 1 Gold, 2 Village")

    for deckString in deckStrings:
        deck = cardsFromDeckString(deckString)
        res = simDeckTurn(deck, NUM_SAMPLES)

        # Display Stats
        if (res.averageActionsPlayed + res.averageActionsDiscarded == 0):
            actionPlayRate = -1
        else:
            actionPlayRate = res.averageActionsPlayed / (res.averageActionsPlayed + res.averageActionsDiscarded)
        print("%s: ATM(calcATM) %.2f(%.2f) actionRate(calcTerminalRate): %.2f(%.2f)" % (deckString, res.moneyDist[0], calcATMReferenceBot.calcATM_Math(deck), actionPlayRate, calcATMReferenceBot.terminalPlayProbability(deck)))

# GO
# gameTests()
turnTests()
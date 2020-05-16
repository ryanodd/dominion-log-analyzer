import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math

from utils.stringUtils import cardsFromDeckString
from sim.gameSim import simGame
from sim.turnSim import simDeckTurn
from bot.bot import Bot

class GameTestSet:
    bots = []
    shopCards = []

def gameTests():

    NUM_SAMPLES = 2000

    mathBot = Bot({"calcATMMath": True})

    shopStrings = {}
    shopStrings['classic'] = "1 Smithy, 1 Market, 1 Village, 1 Festival"
    

    games = []
    games.append(GameTestSet([mathBot], [cardsFromDeckString(shopStrings['classic'])]))

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
    NUM_SAMPLES = 100000

    calcATMReferenceBot = Bot({"useCalcATM": False})

    deckStrings = []
    deckStrings.append("7 Copper, 3 Estate, 4 Silver, 2 Gold")
    deckStrings.append("7 Copper, 3 Estate, 3 Silver, 2 Smithy, 1 Gold")

    for deckString in deckStrings:
        deck = cardsFromDeckString(deckString)
        res = simDeckTurn(deck, NUM_SAMPLES)

        # Display Stats
        if (res.averageActionsPlayed + res.averageActionsDiscarded == 0):
            actionPlayRate = -1
        else:
            actionPlayRate = res.averageActionsPlayed / (res.averageActionsPlayed + res.averageActionsDiscarded)
        print("%s: ATM(M2) %.2f(%.0f) calcATM: %.2f actionRte(M2): %.2f(%.0f)" % (deckString, res.moneyDist[1], math.sqrt(res.moneyDist[2]), calcATMReferenceBot.calcATM(deck), actionPlayRate, math.sqrt(res.actionDist[2])))

# GO
turnTests()
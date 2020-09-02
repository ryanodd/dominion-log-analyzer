import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from utils.stringUtils import cardsFromDeckString
from sim.gameSim import simGame
from sim.turnSim import simDeckTurn
from bot.bot import Bot
from utils.dominionOnlineLogParser.logParser import logToGameState

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
    #deckStrings.append("7 Copper, 3 Estate, 3 Silver, 2 Smithy, 1 Gold")
    #deckStrings.append("7 Copper, 3 Estate, 3 Silver, 4 Smithy, 1 Gold")
    #deckStrings.append("7 Copper, 3 Estate, 3 Silver, 2 Smithy, 1 Gold, 2 Village")
    deckStrings.append("19 Copper, 1 Smithy")
    deckStrings.append("18 Copper, 2 Smithy")
    deckStrings.append("17 Copper, 3 Smithy")
    deckStrings.append("16 Copper, 4 Smithy")
    deckStrings.append("15 Copper, 5 Smithy")
    deckStrings.append("15 Copper, 4 Smithy")
    deckStrings.append("15 Copper, 3 Smithy")
    deckStrings.append("15 Copper, 2 Smithy")
    deckStrings.append("15 Copper, 1 Smithy")
    
    for deckString in deckStrings:
        deck = cardsFromDeckString(deckString)
        res = simDeckTurn(deck, NUM_SAMPLES)

        # Display Stats
        if (res.averageActionsPlayed + res.averageActionsDiscarded == 0):
            actionPlayRate = -1
        else:
            actionPlayRate = res.averageActionsPlayed / (res.averageActionsPlayed + res.averageActionsDiscarded)
        print("%s: ATM: %.2f actionRate: %.2f ATC: %.2f" % (deckString, res.moneyDist[0], actionPlayRate, res.averageCards))


def logTest():
    logStr = log = "\
    Game #52848131, unrated.\
    \
    L starts with 7 Coppers.\
    L starts with 3 Estates.\
    J starts with 7 Coppers.\
    J starts with 3 Estates.\
    L shuffles their deck.\
    L draws 5 cards.\
    J shuffles their deck.\
    J draws 3 Coppers and 2 Estates.\
    \
    Turn 1 - Lord Rattington\
    L plays 3 Coppers. (+$3)\
    L buys and gains a Silver.\
    L draws 5 cards.\
    \
    Turn 1 - Jazzercise\
    J plays 3 Coppers. (+$3)\
    J buys and gains a Silver.\
    J draws 4 Coppers and an Estate.\
    \
    Turn 2 - Lord Rattington\
    L plays 4 Coppers. (+$4)\
    L buys and gains an Oracle.\
    L shuffles their deck.\
    L draws 5 cards.\
    \
    Turn 2 - Jazzercise\
    J plays 4 Coppers. (+$4)\
    J buys and gains a Groom.\
    J shuffles their deck.\
    J draws 2 Coppers, a Silver, an Estate and a Groom.\
    \
    Turn 3 - Lord Rattington\
    L plays an Oracle.\
    L reveals 2 Estates.\
    L discards 2 Estates.\
    J reveals 2 Coppers.\
    J discards 2 Coppers.\
    L draws 2 cards.\
    L plays 5 Coppers. (+$5)\
    L buys and gains a Patrol.\
    L shuffles their deck.\
    L draws 5 cards.\
    \
    Turn 3 - Jazzercise\
    \
    Players can see spectator chat\
    Joining game #52848131 on tokyo.\
    message\
    "
    gameState = logToGameState(log)
    for player in gameState.players:
        for card in player.deck:
            print(card.name)
    

# GO
#gameTests()
#turnTests()
logTest
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from game import *
from bigMoneyBot import BigMoneyBot
import factory

NUM_SAMPLES = 1000

# Not sure if this class should store roundDist like this... Scores may be measured differently later. Store outside?
class GameSet:
    def __init__(self, name, bots, cards):
        self.name = name
        self.bots = bots
        self.cards = cards
        self.samples = []
        self.roundDist = {}

games = []

basicBot = BigMoneyBot("BigMoney_Basic", {})
games.append(GameSet("Basic", [basicBot], []))
smithyBot = BigMoneyBot("BigMoney_Smithy", {})
games.append(GameSet("Smithy", [smithyBot], [factory.smithy()]))

# onePatienceBot = BigMoneyBot("BigMoney_1Patience", {"provincePatience": 1})
# games.append(GameSet("1Patience", [onePatienceBot], []))
# twoPatienceBot = BigMoneyBot("BigMoney_2Patience", {"provincePatience": 2})
# games.append(GameSet("2Patience", [twoPatienceBot], []))

# Run games
for g in games:
    for i in range(NUM_SAMPLES):
        g.samples.append(Game(g.bots, g.cards))
        g.samples[-1].run()

# Collect Stats
for g in games:
    for sample in g.samples:
        roundsTaken = sample.board.round
        if (roundsTaken in g.roundDist):
            g.roundDist[roundsTaken] += 1
        else:
            g.roundDist[roundsTaken] = 1

# Display Stats
for g in games:
    # print(g.name)
    # for i in range(30):
    #     if (i in g.roundDist):
    #         print("%s rounds: %s" % (i, g.roundDist[i]))
    # print()
    plotDataFrame = pd.DataFrame({"Rounds": list(g.roundDist.keys()), "Frequency": list(g.roundDist.values())})
    sns.lineplot(data=plotDataFrame, x="Rounds", y="Frequency", label=g.name), 
plt.show()

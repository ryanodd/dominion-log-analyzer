# Data display
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from game import *
from bigMoneyBot import Bot
import cardFactory

NUM_SAMPLES = 2000

# Not sure if this class should store roundDist like this... Scores may be measured differently later. Store outside?
class GameSet:
    def __init__(self, name, bots, cards):
        self.name = name
        self.bots = bots
        self.cards = cards
        self.samples = []
        self.roundDist = {}

games = []

basicBot = Bot({})
games.append(GameSet("Basic", [basicBot], []))

smithyBot = Bot({})
games.append(GameSet("Smithy", [smithyBot], [cardFactory.smithy()]))

# marketBot = Bot({"cardsPerTerminal": 8})
# games.append(GameSet("Market", [marketBot], [cardFactory.market()]))

# laboratoryBot = Bot({"cardsPerTerminal": 8})
# games.append(GameSet("Laboratory", [laboratoryBot], [cardFactory.laboratory()]))

chapelBot = Bot({"chapelEnabled": True})
games.append(GameSet("Chapel", [chapelBot], [cardFactory.chapel()]))

chapelSmithyBot = Bot({"chapelEnabled": True, "provincePatience": 1})
games.append(GameSet("Chapel/Smithy", [chapelSmithyBot], [cardFactory.chapel(), cardFactory.smithy()]))

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

import math

from stringUtils import cardsFromDeckString
from turnSim import simDeckTurn
from bot import Bot

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
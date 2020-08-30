from game.gameController import GameController
from bot.bot import Bot
from game.card.cardFactory import getCard

class GameSimInfo:
    def __init__(self, roundDist):
        self.roundDist = roundDist

def simGame(bots, shopCards, numSamples):
    samples = []

    # Run games
    for _ in range(numSamples):
        samples.append(Game(bots, shopCards))
        samples[-1].run()

    # Collect Stats
    roundDist = {}
    for sample in samples:
        roundsTaken = sample.round
        if (roundsTaken in roundDist):
            roundDist[roundsTaken] += 1
        else:
            roundDist[roundsTaken] = 1
        
    return GameSimInfo(roundDist)

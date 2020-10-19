from game.gameController import GameController
from game.gameState import GameState
from game.playerState import PlayerState
from bot.bot import Bot
from game.card.gCardFactory import getCard

class GameSimInfo:
    def __init__(self, roundDist):
        self.roundDist = roundDist

def simGame(bots, deckCards, shopCards, numSamples):
    samples = []

    # Run games
    for _ in range(numSamples):
        players = []
        for _ in range(len(bots)):
            players.append(PlayerState('bob', deckCards))
        game = GameState(players, shopCards)
        samples.append(GameController(game, bots))
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

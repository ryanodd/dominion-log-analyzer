import copy

from utils.log import logError, logGame
from game.board import Board
from game.player import Player

class Game:
    def __init__(self, bots, cards):
        self.board = Board(cards, len(bots))
        self.players = []
        for b in bots:
            self.players.append(Player(self.board, copy.deepcopy(b))) # This copy doesn't need to be deep at the moment.

    # Current win condition is owning 4 provinces
    def isOver(self):
        for i in range(len(self.players)):
            deck = self.players[i].totalDeck()
            provinces = 0
            for j in range(len(deck)):
                if (deck[j].name == "Province"):
                    provinces += 1
            if (provinces >= 4):
                return True
        return False

    def run(self):
        while True:
            self.board.round += 1
            logGame("Round %s begins" % self.board.round)
            for i in range(len(self.players)):
                self.players[i].turn()
                if self.isOver():
                    logGame("Game Over! Ended after round %s" % self.board.round)
                    return

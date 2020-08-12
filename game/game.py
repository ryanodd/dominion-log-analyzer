import copy

from utils.log import logError, logGame
from game.shop import Shop
from game.player import Player

class Game:
    def __init__(self, bots, cards):
        self.shop = Shop(cards, len(bots))
        self.players = []
        for b in bots:
            self.players.append(Player(self, b)) # This copy doesn't need to be deep at the moment.
        self.shop = Shop(cards, len(self.players))
        self.trash = []
        self.round = 0

    def shouldStopGame(self):
        if (True):
            return self.isGameOver()
        else:
            return self.hasSomeoneGainedFourProvinces()

    def hasSomeoneGainedFourProvinces(self):
        for i in range(len(self.players)):
            deck = self.players[i].totalDeck()
            provinces = 0
            for j in range(len(deck)):
                if (deck[j].name == "Province"):
                    provinces += 1
            if (provinces >= 4):
                return True
        return False

    def isGameOver(self):
        # Assumes that this is only called at the end of every turn
        if shop.listings['Province'].quantity == 0: # TODO: Check for Colony
            return True

        depletedPileCount = 0
        for listing in shop.listings:
            if listing.quantity == 0: # TODO: make sure not to check non-pileout piles e.g. Tournament Prizes
                depletedPileCount += 1
        return depletedPileCount >= 3
            
    # TODO: move player turn logic into this class
    def run(self):
        while True:
            self.round += 1
            logGame("Round %s begins" % self.round)
            for i in range(len(self.players)):
                self.players[i].turn()
                if self.shouldStopGame():
                    logGame("Game Over! Ended after round %s" % self.round)
                    return

    # TODO: move into gameUtils
    def otherPlayers(self, originalPlayer):
        returnPlayers = []
        for player in self.players:
            if (player != originalPlayer):
                returnPlayers.append(player)
        if (len(returnPlayers) == len(self.players)):
            logError("otherPlayers: did not find match...")
        return returnPlayers

    def gain(self, shopIndex):
        # log?
        return self.shop.pop(shopIndex)
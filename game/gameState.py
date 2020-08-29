import copy
from enum import Enum

from utils.log import logError, logGame
from game.shop import Shop
from game.playerState import PlayerState
from game.card.card import CardType
from game.choice import Choice

# TODO: TRULY figure out what information needed to run the game is not captured by GameState.
# Approach: Implement GameLog to make games continuable if you have GameState + GameLog?
# Approach: Store everrrryything in the state. Current turn phase, currently played card choice #, etc, SOMETHING UNFORSEEN
# Snowy Village
# Merchant (if you implement it properly)
#

class TurnPhase(Enum):
    ACTION: 0
    BUY: 1
    BOUGHT: 2 # After first buy (can't play treasure)

class GameState:
    def __init__(self, shop, players):
        self.shop = shop
        self.players = players
        self.trash = []
        self.cardStoreStack = [] # stores "buckets" of cards in a stack
        self.round = 0
        self.currentPlayerIndex = 0
        self.currentTurnPhase = TurnPhase.ACTION # is this right?
        # self.log = ?

    def isGameOverAtEndOfTurn(self):
        if self.shop.listings['Province'].quantity == 0: # TODO: Check for Colony
            return True

        depletedPileCount = 0
        for listing in self.shop.listings:
            if listing.quantity == 0: # TODO: make sure not to check non-pileout piles e.g. Tournament Prizes
                depletedPileCount += 1
        return depletedPileCount >= 3

    def currentPlayer(self):
        return self.players[self.currentPlayerIndex]

    # woah does this equality check work? Is it slow?
    def otherPlayers(self, originalPlayer):
        returnPlayers = []
        for player in self.players:
            if (player != originalPlayer):
                returnPlayers.append(player)
        if (len(returnPlayers) == len(self.players)):
            logError("otherPlayers: did not find match...")
        return returnPlayers
import copy

from utils.log import logError, logGame
from game.shop import Shop
from game.player import Player
from game.card.card import CardType
from game.choices import Choice

# TODO: These should take over the data model for Game & Player

class PlayerState:
  def __init__(self, player):
    self.deck = player.deck
    self.discard = player.discard
    self.hand = player.hand
    self.vpTokens = player.vp
    
    # mid-turn relevance?
    self.play = player.play
    self.money = player.money
    self.actions = player.actions

class GameState:
    def __init__(self, game):
        self.shop = game.shop
        self.players = []
        for player in game.players:
            self.players.append(PlayerState(player))

        self.trash = game.trash
        self.round = game.round
        self.currentPlayerIndex = game.currentPlayerIndex

    def isGameOver(self):
        # Assumes that this is only called at the end of every turn
        if self.shop.listings['Province'].quantity == 0: # TODO: Check for Colony
            return True

        depletedPileCount = 0
        for listing in self.shop.listings:
            if listing.quantity == 0: # TODO: make sure not to check non-pileout piles e.g. Tournament Prizes
                depletedPileCount += 1
        return depletedPileCount >= 3

    def currentPlayer(self):
        return self.players[self.currentPlayerIndex]

    def otherPlayers(self, originalPlayer):
        returnPlayers = []
        for player in self.players:
            if (player != originalPlayer):
                returnPlayers.append(player)
        if (len(returnPlayers) == len(self.players)):
            logError("otherPlayers: did not find match...")
        return returnPlayers
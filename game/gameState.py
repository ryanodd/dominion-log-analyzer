from enum import Enum

from utils.log import logError

# TODO: TRULY figure out what information needed to run the game is not captured by GameState.
# Approach: Implement GameLog to make games continuable if you have GameState + GameLog?
# ^ GameLog could be good anyway for analytics
# Approach: Store everrrryything in the state. Current turn phase, currently played card choice #, etc, SOMETHING UNFORSEEN

# (UP TO DARK AGES) things that can't be implemented:
# Snowy Village
# Merchant (if you implement it properly)
# Duration
# Conspirator (if you implement it properly)
# Bridge!!!!! Not just the shop
# Haven needs changes to CardStoreStack? Or should it be in play. Where does that card go? Where is its info (to hand next turn) stored?
# Moat / Lighthouse obvi
# Outpost
# "When you discard this from play" Alchemist, Herbalist
# Posession
# Grand Market
# Fool's Gold
# "When you buy a card" Goons/Merchant Guild/Lackeys/Hoard/Duchess
# "when you buy this card" Lackeys/Silk Merchant/Cache/IGG
# Young Witch (bane card)
# Inn "when you gain" has to happen AFTER the gain
# Hermit is a big challenge "If you bought a card this turn"

class TurnPhase(Enum):
    ACTION = 0
    BUY = 1
    BOUGHT = 2 # After first buy (can't play treasure). Could replace with 'hasBoughtThisTurn' flag
    CLEANUP = 3

class GameState:
    def __init__(self, shop, players):
        self.shop = shop
        self.players = players
        self.trash = []
        self.cardStoreStack = [] # stores "buckets" of cards in a stack
        self.round = 0 # actually starts at 1
        self.currentPlayerIndex = 0
        self.currentTurnPhase = TurnPhase.ACTION # is this right?
        # self.log = ?

    def incrementTurn(self):
        self.currentTurnPhase = TurnPhase.ACTION
        if self.round == 0:
            self.round = 1
        elif self.currentPlayerIndex == len(self.players) - 1:
            self.round += 1
            self.currentPlayerIndex = 0
        else:
            self.currentPlayerIndex = 0

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
import copy
from enum import Enum

from utils.log import logError, logGame
from game.shop import Shop
from game.player import Player
from game.card.card import CardType
from game.choice import Choice, ChoiceID, getChoice
from game.gameState import GameState

class GainType(Enum):
    DISCARD = 0
    DECK = 1

class Game:
    def __init__(self, bots, cards):
        self.shop = Shop(cards, len(bots))
        self.players = []
        for b in bots:
            self.players.append(Player(self, b))
        self.shop = Shop(cards, len(self.players))
        self.trash = []
        self.cardStoreStack = [] # stores "buckets" of cards in a stack
        self.round = 0
        self.currentPlayerIndex = 0

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
        if self.shop.listings['Province'].quantity == 0: # TODO: Check for Colony
            return True

        depletedPileCount = 0
        for listing in self.shop.listings:
            if listing.quantity == 0: # TODO: make sure not to check non-pileout piles e.g. Tournament Prizes
                depletedPileCount += 1
        return depletedPileCount >= 3
            
    # TODO: move player turn logic into this class
    def run(self):
        while True:
            self.round += 1
            logGame("Round %s begins" % self.round)
            while not self.shouldStopGame:
                self.playerTurn(self.players[self.currentPlayerIndex])
                self.currentPlayerIndex = (self.currentPlayerIndex + 1) % len(self.players)
            logGame("Game Over! Ended after round %s" % self.round)
            return

    def playerTurn(self, player):
        player.money = 0
        player.actions = 1
        player.buys = 1
        # log("%s's turn begins" % self.bot.name)
        player.log.turnStart(player.hand)
        self.playerActionPhase(player)
        self.playerBuyPhase(player)
        self.playerCleanupPhase(player)


    def playerActionPhase(self, player):
        # Actions
        while player.actions and player.hasTypeInHand(CardType.ACTION):
            actionChoice = player.bot.choose(getChoice(ChoiceID.ACTION), GameState(self), self.currentPlayerIndex)
            if (actionChoice == -1):
                break
            elif (actionChoice >= 0 and actionChoice < len(player.hand)
            and CardType.ACTION in player.hand[actionChoice].types):
                # perform action
                actionCard = player.hand.pop(actionChoice)
                player.play.append(actionCard)
                player.actions -= 1
                player.log.playAction(actionCard)
                actionCard.steps(player, self)
            else:
                logError("Invalid action choice: %s" % actionChoice)

    def playerBuyPhase(self, player): 
        # Playing Treasures
        while player.hasTypeInHand(CardType.TREASURE):
            treasureChoice = player.bot.choose(getChoice(ChoiceID.TREASURE), GameState(self), self.currentPlayerIndex)
            if (treasureChoice == -1):
                break
            elif (treasureChoice >= 0 and treasureChoice < len(player.hand)
            and CardType.TREASURE in player.hand[treasureChoice].types):
                # play treasure
                treasureCard = player.hand.pop(treasureChoice)
                player.play.append(treasureCard)
                player.log.playTreasure(treasureCard)
                treasureCard.steps(player, self)
            else:
                logError("Invalid treasure choice: %s" % treasureChoice)
        # Buys
        player.log.buyStart(player.money, player.buys)
        while player.buys:
            buyChoice = player.bot.choose(getChoice(ChoiceID.BUY), GameState(self), self.currentPlayerIndex)
            if (buyChoice == -1):
                break
            elif (buyChoice >= 0 and buyChoice < len(self.shop.listings)
            and player.money >= self.shop.listings[buyChoice].card.cost
            and self.shop.listings[buyChoice].quantity > 0):
                # perform buy
                buyCard = self.gain(buyChoice, self.currentPlayer)
                player.money -= buyCard.cost
                player.discard.append(buyCard)
                player.buys -= 1
                player.log.buy(buyCard)
            else:
                logError("Invalid buy choice: %s" % buyChoice)

    def playerCleanupPhase(self, player):
        player.log.turnEnd(player.hand)
        while player.play:
            player.discard.append(player.play.pop())
        while player.hand:
            player.discard.append(player.hand.pop())
        player.draw(5)

        # log("%s's turn ends" % self.bot.name)
        # Necessary? When is the right time to reset them to their defaults?
        player.money = 0
        player.actions = 0
        player.buys = 0

    def currentPlayer(self):
            return self.players[self.currentPlayerIndex]

    # TODO: move into gameUtils
    def otherPlayers(self, originalPlayer):
        returnPlayers = []
        for player in self.players:
            if (player != originalPlayer):
                returnPlayers.append(player)
        if (len(returnPlayers) == len(self.players)):
            logError("otherPlayers: did not find match...")
        return returnPlayers

    #Returns a reference to the gained card for convenience
    def gain(self, cardName, player, gainType=GainType.DISCARD):
        # log?
        return player.gain(self.shop.pop(cardName), gainType)

    def newCardStore(self):
        return self.cardStoreStack.append([])[-1]

    def popCardStore(self):
        return self.cardStoreStack.pop()
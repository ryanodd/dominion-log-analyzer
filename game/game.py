import copy

from utils.log import logError, logGame
from game.shop import Shop
from game.player import Player
from game.card.card import CardType
from game.choices import Choice

class Game:
    def __init__(self, bots, cards):
        self.shop = Shop(cards, len(bots))
        self.players = []
        for b in bots:
            self.players.append(Player(self, b))
        self.shop = Shop(cards, len(self.players))
        self.trash = []
        self.round = 0
        self.currentPlayerIndex = 0
        # TODO: store stack for things like the 2 sentry cards. Cards should not briefly live inside card.steps().

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
            while not self.shouldStopGame:
                self.playerTurn(self.players[self.currentPlayerIndex])
                self.currentPlayerIndex = (currentPlayerIndex + 1) % len(self.players)
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
            actionChoice = player.bot.choose(Choice.ACTION, GameState(self))
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
            treasureChoice = player.bot.choose(Choice.TREASURE, GameState(self))
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
            buyChoice = player.bot.choose(Choice.BUY, GameState(self))
            if (buyChoice == -1):
                break
            elif (buyChoice >= 0 and buyChoice < len(self.shop.listings)
            and player.money >= self.shop.listings[buyChoice].card.cost
            and self.shop.listings[buyChoice].quantity > 0):
                # perform buy
                buyCard = self.gain(buyChoice)
                player.money -= buyCard.cost
                player.discard.append(buyCard)
                player.buys -= 1
                player.log.buy(buyCard)
            else:
                logError("Invalid buy choice: %s" % buyChoice)

    def playerCleanupPhase(self, player):
        player.log.turnEnd(self.hand)
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

    def gain(self, shopIndex):
        # log?
        return self.shop.pop(shopIndex)
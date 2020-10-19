from enum import Enum

from utils.log import logError, logGame
from game.playerState import GainType
from game.card.gCard import CardType
from game.choice import ChoiceID, getChoice

class GameEvent(Enum):
    GAME_START = 0
    GAME_END = 1

    TURN_START = 2
    TURN_END = 3

    CARD_PLAY = 4
    CARD_LEAVE_PLAY = 5 # ?? should this be a thing ??
    CARD_BUY = 6
    CARD_GAIN = 7
    CARD_DISCARD = 8
    CARD_REVEAL = 9

    PLAYER_ATTACK = 10
    # What to do about attacks? Skipping the steps is tough.
    # Trader introduces a similar challenge ^ things (so far, attacks & gains) need to be cancellable on reaction

class GameController:
    def __init__(self, gameState, bots):
        self.gameState = gameState
        self.bots = bots

    def shouldStopGame(self):
        if (True):
            return self.gameState.isGameOver()
        else:
            return self.hasSomeoneGainedFourProvinces()

    def hasSomeoneGainedFourProvinces(self):
        for i in range(len(self.gameState.players)):
            deck = self.gameState.players[i].totalDeck()
            provinces = 0
            for j in range(len(deck)):
                if (deck[j].name == "Province"):
                    provinces += 1
            if (provinces >= 4):
                return True
        return False

    def run(self):
        game = self.gameState
        for player in game.players:
            player.shuffleDeck()
            player.draw(5)
        while True:
            game.round += 1
            logGame("Round %s begins" % game.round)
            while not self.shouldStopGame:
                game.currentPlayerTurn(game.players[game.currentPlayerIndex])
                game.currentPlayerIndex = (game.currentPlayerIndex + 1) % len(game.players)
            logGame("Game Over! Ended after round %s" % game.round)
            return

    def currentPlayerTurn(self):
        game = self.gameState
        player = game.players[game.currentPlayerIndex]

        player.money = 0
        player.actions = 1
        player.buys = 1
        # log("%s's turn begins" % self.bot.name)
        # player.log.turnStart(player.hand)
        self.currentPlayerActionPhase()
        self.currentPlayerBuyPhase()
        self.currentPlayerCleanupPhase()


    def currentPlayerActionPhase(self):
        game = self.gameState
        player = game.players[game.currentPlayerIndex]
        while player.actions and player.hasTypeInHand(CardType.ACTION):
            actionChoice = self.bots[game.currentPlayerIndex].choose(getChoice(ChoiceID.ACTION), game, game.currentPlayerIndex)
            if (actionChoice == -1):
                break
            elif (actionChoice >= 0 and actionChoice < len(player.hand)
            and CardType.ACTION in player.hand[actionChoice].types):
                # perform action
                actionCard = player.hand.pop(actionChoice)
                player.play.append(actionCard)
                player.actions -= 1
                player.log.playAction(actionCard)
                actionCard.steps(player, game)
            else:
                logError("Invalid action choice: %s" % actionChoice)

    def currentPlayerBuyPhase(self):
        game = self.gameState
        player = game.players[game.currentPlayerIndex]
        # Playing Treasures
        while player.hasTypeInHand(CardType.TREASURE):
            treasureChoice = self.bots[game.currentPlayerIndex].choose(getChoice(ChoiceID.TREASURE), game, game.currentPlayerIndex)#!!!!!!!!!!
            if (treasureChoice == -1):
                break
            elif (treasureChoice >= 0 and treasureChoice < len(player.hand)
            and CardType.TREASURE in player.hand[treasureChoice].types):
                # play treasure
                treasureCard = player.hand.pop(treasureChoice)
                player.play.append(treasureCard)
                player.log.playTreasure(treasureCard)
                treasureCard.steps(player, game)
            else:
                logError("Invalid treasure choice: %s" % treasureChoice)
        # Buys
        player.log.buyStart(player.money, player.buys)
        while player.buys:
            buyChoice = self.bots[game.currentPlayerIndex].choose(getChoice(ChoiceID.BUY), game, game.currentPlayerIndex)
            if (buyChoice == -1):
                break
            elif (buyChoice >= 0 and buyChoice < len(game.shop.listings)
            and player.money >= game.shop.listings[buyChoice].card.cost
            and game.shop.listings[buyChoice].quantity > 0):
                # perform buy
                buyCard = game.player.gain(buyChoice, game.currentPlayer)
                player.money -= buyCard.cost
                player.discard.append(buyCard)
                player.buys -= 1
                player.log.buy(buyCard)
            else:
                logError("Invalid buy choice: %s" % buyChoice)

    def currentPlayerCleanupPhase(self):
        game = self.gameState
        player = game.players[game.currentPlayerIndex]
        while player.hand: # This order is correct: see Alchemist
            player.discard.append(player.hand.pop())
        while player.play:
            player.discard.append(player.play.pop())
        player.draw(5)

        # log("%s's turn ends" % self.bot.name)
        # Necessary? When is the right time to reset them to their defaults?
        player.money = 0
        player.actions = 0
        player.buys = 0

    # Returns a reference to the gained card for convenience
    def gain(self, cardName, playerIndex, gainType=GainType.DISCARD):
        # log?
        return self.gameState.players[playerIndex].gain(self.gameState.shop.pop(cardName), gainType)
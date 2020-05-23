import random

from utils.log import PlayerLog, logError
from game.card import CardType
from game.cardFactory import getCard
from game.choices import Choice

class Player:
    def __init__(self, board, bot, deck = []):
        self.board = board
        self.bot = bot
        self.log = PlayerLog()

        if (deck):
            self.deck = deck
        else:
            self.deck = []
            self.deck.append(getCard('Copper'))
            self.deck.append(getCard('Copper'))
            self.deck.append(getCard('Copper'))
            self.deck.append(getCard('Copper'))
            self.deck.append(getCard('Copper'))
            self.deck.append(getCard('Copper'))
            self.deck.append(getCard('Copper'))
            self.deck.append(getCard('Estate'))
            self.deck.append(getCard('Estate'))
            self.deck.append(getCard('Estate'))
        
        self.discard = []
        self.hand = []
        self.play = []
        self.money = 0
        self.vp = 0

        self.shuffleDeck()
        self.draw(5)

    def draw(self, num):
        for _ in range(num):
            if (len(self.deck) <= 0):
                self.reshuffle()
                if (len(self.deck) <= 0):
                    #still empty after reshuffling, can't draw
                    return
            self.hand.append(self.deck.pop())

    def shuffleDeck(self):
        random.shuffle(self.deck)
    
    def reshuffle(self):
        self.deck = self.discard.copy()
        self.discard = []
        # MAKE SURE THIS WORKS^^^ PASS BY REF SCARES ME
        self.shuffleDeck()

    def turn(self):
        self.money = 0
        self.actions = 1
        self.buys = 1
        # log("%s's turn begins" % self.bot.name)
        self.log.turnStart(self.hand)

        # Actions
        while self.actions and self.hasTypeInHand(CardType.ACTION):
            actionChoice = self.bot.choose(Choice.ACTION, self, self.board)
            if (actionChoice == -1):
                break
            elif (actionChoice >= 0 and actionChoice < len(self.hand)
            and CardType.ACTION in self.hand[actionChoice].types):
                # perform action
                actionCard = self.hand.pop(actionChoice)
                self.play.append(actionCard)
                self.actions -= 1
                self.log.playAction(actionCard)
                actionCard.steps(self, self.board)
            else:
                logError("Invalid action choice: %s" % actionChoice)

        # Playing Treasures
        while self.hasTypeInHand(CardType.TREASURE):
            treasureChoice = self.bot.choose(Choice.TREASURE, self, self.board)
            if (treasureChoice == -1):
                break
            elif (treasureChoice >= 0 and treasureChoice < len(self.hand)
            and CardType.TREASURE in self.hand[treasureChoice].types):
                # play treasure
                treasureCard = self.hand.pop(treasureChoice)
                self.play.append(treasureCard)
                self.log.playTreasure(treasureCard)
                treasureCard.steps(self, self.board)
            else:
                logError("Invalid treasure choice: %s" % treasureChoice)
        # Buys
        self.log.buyStart(self.money, self.buys)
        while self.buys:
            buyChoice = self.bot.choose(Choice.BUY, self, self.board)
            if (buyChoice == -1):
                break
            elif (buyChoice >= 0 and buyChoice < len(self.board.shop)
            and self.money >= self.board.shop[buyChoice].card.cost
            and self.board.shop[buyChoice].quantity > 0):
                # perform buy
                buyCard = self.board.buy(buyChoice)
                self.money -= buyCard.cost
                self.discard.append(buyCard)
                self.buys -= 1
                self.log.buy(buyCard)
            else:
                logError("Invalid buy choice: %s" % buyChoice)

        # Cleanup
        self.log.turnEnd(self.hand)
        while self.play:
            self.discard.append(self.play.pop())
        while self.hand:
            self.discard.append(self.hand.pop())
        self.draw(5)

        # log("%s's turn ends" % self.bot.name)
        # Necessary?
        self.money = 0
        self.actions = 0
        self.buys = 0

    def totalDeck(self):
        return self.deck + self.hand + self.discard + self.play

    def hasTypeInHand(self, type):
        for card in self.hand:
            if(type in card.types):
                return True
        return False

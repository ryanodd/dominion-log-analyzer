import random

from log import *
from card import *
import factory

class Player:
    def __init__(self, board, bot):
        self.board = board
        self.bot = bot

        self.deck = []
        self.deck.append(factory.copper())
        self.deck.append(factory.copper())
        self.deck.append(factory.copper())
        self.deck.append(factory.copper())
        self.deck.append(factory.copper())
        self.deck.append(factory.copper())
        self.deck.append(factory.copper())
        self.deck.append(factory.estate())
        self.deck.append(factory.estate())
        self.deck.append(factory.estate())
        self.discard = []
        self.hand = []
        self.play = []
        self.money = 0
        self.vp = 0

        self.shuffleDeck()
        self.draw(5)

    def draw(self, num):
        for i in range(num):
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
        logCards(self.hand, "Hand")

        # Actions
        while self.actions:
            actionChoice = self.bot.choose('action', self, self.board)
            if (actionChoice == -1):
                break
            elif (actionChoice >= 0 and actionChoice < len(self.hand)
            and CardType.ACTION in self.hand[actionChoice].types):
                # perform action
                actionCard = self.hand.pop(actionChoice)
                self.play.append(actionCard)
                self.actions -= 1
                log("%s plays action: %s" % (self.bot.name, actionCard.name))
                actionCard.steps(self, self.board)
            else:
                logError("Invalid action choice: %s" % actionChoice)

        # Playing Treasures
        while True:
            treasureChoice = self.bot.choose('treasure', self, self.board)
            if (treasureChoice == -1):
                break
            elif (treasureChoice >= 0 and treasureChoice < len(self.hand)
            and CardType.TREASURE in self.hand[treasureChoice].types):
                # play treasure
                treasureCard = self.hand.pop(treasureChoice)
                self.play.append(treasureCard)
                # log("%s plays treasure: %s" % (self.bot.name, treasureCard.name))
                treasureCard.steps(self, self.board)
            else:
                logError("Invalid treasure choice: %s" % treasureChoice)
        # Buys
        while self.buys:
            buyChoice = self.bot.choose('buy', self, self.board)
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
                log("%s buys: %s" % (self.bot.name, buyCard.name))
            else:
                logError("Invalid buy choice: %s" % buyChoice)

        # Cleanup
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

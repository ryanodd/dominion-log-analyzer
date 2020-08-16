import random

from utils.log import PlayerLog, logError
from game.card.card import CardType
from game.card.cardFactory import getCard
from game.choice import Choice
from game.game import GainType

class Player:
    def __init__(self, game, bot, deck = []):
        self.game = game
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
        self.vpTokens = 0

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

    # Returns reference to card for convenience
    def gain(self, card, gainType=GainType.DISCARD):
        if gainType == GainType.DISCARD:
            self.discard.append(card)
        elif gainType == GainType.DECK:
            self.deck.append(card)
        return card

    def totalDeck(self):
        return self.deck + self.hand + self.discard + self.play

    def hasTypeInHand(self, type):
        for card in self.hand:
            if(type in card.types):
                return True
        return False

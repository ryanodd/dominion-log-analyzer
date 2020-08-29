import random
from enum import Enum

from utils.log import PlayerLog, logError
from game.card.card import CardType
from game.card.cardFactory import getCard
from game.choice import Choice

class GainType(Enum):
    DISCARD = 0
    DECK = 1
    HAND = 2

class PlayerState:
  def __init__(self, deck = []):
    if deck:
        self.deck = deck
    else:
        for _ in range(7):
            self.deck.append(getCard('Copper'))
        for _ in range(3):
            self.deck.append(getCard('Estate'))
    self.discard = []
    self.hand = []
    self.play = []
    
    self.money = 0
    self.actions = 0
    self.buys = 0

    self.vpTokens = 0

    def draw(self, num):
        for _ in range(num):
            if (len(self.deck) <= 0):
                self.reshuffle()
                if (len(self.deck) <= 0):
                    #still empty after reshuffling, can't draw
                    return
            self.hand.append(self.deck.pop())

    def deckPop(self):
        if len(self.deck) <= 0:
            self.reshuffle()
            if len(self.deck) <= 0:
                return None
        return self.deck.pop()

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

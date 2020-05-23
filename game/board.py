from game.cardFactory import getCard
from utils.log import logError

class Listing:
    def __init__(self, card, quantity):
        self.card = card
        self.quantity = quantity

class Board:
    def __init__(self, cards, numPlayers):
        self.shop = []
        self.trash = []
        self.round = 0

        victoryAmount = 12
        if (numPlayers <= 2):
            victoryAmount = 8
            
        self.shop.append(Listing(getCard('Estate'), victoryAmount))
        self.shop.append(Listing(getCard('Duchy'), victoryAmount))
        self.shop.append(Listing(getCard('Province'), victoryAmount))
        self.shop.append(Listing(getCard('Curse'), 30))
        self.shop.append(Listing(getCard('Copper'), 60))
        self.shop.append(Listing(getCard('Silver'), 40))
        self.shop.append(Listing(getCard('Gold'), 30))

        for i in range(len(cards)):
            self.shop.append(Listing(cards[i], 10))
    
    def buy(self, buyChoice):
        if (buyChoice < 0 or buyChoice >= len(self.shop)):
            logError("Invalid buy choice: %s" % buyChoice)
        return self.shop[buyChoice].card

    def gain(self, gainChoice):
        if (gainChoice < 0 or gainChoice >= len(self.shop)):
            logError("Invalid gain choice: %s" % gainChoice)
        return self.shop[gainChoice].card

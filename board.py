import factory

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
            
        self.shop.append(Listing(factory.estate(), victoryAmount))
        self.shop.append(Listing(factory.duchy(), victoryAmount))
        self.shop.append(Listing(factory.province(), victoryAmount))
        self.shop.append(Listing(factory.curse(), 30))
        self.shop.append(Listing(factory.copper(), 60))
        self.shop.append(Listing(factory.silver(), 40))
        self.shop.append(Listing(factory.gold(), 30))

        for i in range(len(cards)):
            self.shop.append(Listing(cards[i], 10))
    
    def buy(self, buyChoice):
        if (buyChoice < 0 or buyChoice >= len(self.shop)):
            logError("Invalid buy choice: %s" % buyChoice)
        return self.shop[buyChoice].card

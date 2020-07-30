from card.cardFactory import getCard
from utils.log import logError

class Listing:
    def __init__(self, card, quantity):
        self.card = card
        self.quantity = quantity
        self.cost = card.cost

class Shop:
    def __init__(self, cards, numPlayers):
        self.listings = []

        victoryAmount = 12
        if (numPlayers <= 2):
            victoryAmount = 8

        # TODO: Eventually, this shouldn't live here (and this shouldn't take in numPlayers)
        self.listings.append(Listing(getCard('Estate'), victoryAmount))
        self.listings.append(Listing(getCard('Duchy'), victoryAmount))
        self.listings.append(Listing(getCard('Province'), victoryAmount))
        self.listings.append(Listing(getCard('Curse'), 30))
        self.listings.append(Listing(getCard('Copper'), 60))
        self.listings.append(Listing(getCard('Silver'), 40))
        self.listings.append(Listing(getCard('Gold'), 30))

        for i in range(len(cards)):
            self.listings.append(Listing(cards[i], 10))

    def pop(self, index):
        if (index < 0 or index >= len(self.listings)):
            logError("Invalid shop pop choice: %s" % index)
        return self.listings[index].card
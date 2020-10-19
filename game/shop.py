from game.card.gCardFactory import getCard
from utils.log import logError

# TODO: piles of non-duplicate cards need to be supported
# split piles, Knights, Ruins

class Listing:
    def __init__(self, card, quantity):
        self.card = card
        self.quantity = quantity
        self.cost = card.cost # I think altered costs will live in the card (or a decorator ?here?) later. Bridge

class Shop:
    def __init__(self, cards, numPlayers):
        self.listings = {}

        victoryAmount = 12
        if (numPlayers <= 2):
            victoryAmount = 8

        # TODO: Eventually, this shouldn't live here? (and this shouldn't take in numPlayers)
        self.listings['Estate'] = Listing(getCard('Estate'), victoryAmount)
        self.listings['Duchy'] = Listing(getCard('Duchy'), victoryAmount)
        self.listings['Province'] = Listing(getCard('Province'), victoryAmount)
        self.listings['Curse'] = Listing(getCard('Curse'), 30)
        self.listings['Copper'] = Listing(getCard('Copper'), 60)
        self.listings['Silver'] = Listing(getCard('Silver'), 40)
        self.listings['Gold'] = Listing(getCard('Gold'), 30)

        for i in range(len(cards)):
            # TODO: Check for triggers here through trigger/event system e.g. Tournament (merchant will use this system too)
            self.listings[cards[i].name] = Listing(cards[i], 10)

    def pop(self, name):
        if (name not in self.listings):
            logError("Invalid shop pop choice: %s" % name)
        if (self.listings[name].quantity <= 0):
            logError("Invalid shop pop choice: %s, pile empty" % name)
        self.listings[name].quantity -= 0
        return self.listings[name].card
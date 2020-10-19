from utils.log import logError
from bot.botTypes import botValue
from game.card.gCardFactory import getGCard
from game.card.gCard import CardType

# Used as just a parameter for constructing actual Cards.
# This makes it easy to implement every card in the game (more defaults, less writing)
# The Card fields not included in CardParams are generated from the given params.
class CardParams:
    def __init__(self):
        self.money = botValue(0)
        self.draws = botValue(0)
        self.actions = botValue(0)
        self.buys = botValue(0)
        self.vp = botValue(0)

        self.beneficial = botValue(True)

    # Woah. I wonder if this is good or bad. memory & performance
    def reset(self):
        self.__init__()

class Card:
    def __init__(self, name, cardParams):
        self.name = name

        self.money = cardParams.money
        self.draws = cardParams.draws
        self.actions = cardParams.actions
        self.buys = cardParams.buys
        self.vp = cardParams.vp

        # Funny one. Used for bot logic only
        self.beneficial = cardParams.beneficial

        # Careful with these defaults. Not sure about them. Can have card-for-card overriding or one universal alg hmmmmm
        self.cantrip = botValue(False, (self.draws.value > 0 and self.actions.value > 0 ))
        self.extraDraws = botValue(max(0, self.draws.value - 1), self.draws.evaluator, self.draws.message, self.draws.importance)
        self.extraActions = botValue(max(0, self.actions.value - 1), self.actions.evaluator, self.actions.message, self.actions.importance)
        self.terminal = botValue(CardType.ACTION in getGCard(self.name).types and self.actions.value == 0)
        self.stop = botValue(self.draws.value == 0)

# Maps card names to Card objects
cards = {}
cardParams = CardParams()

def createCard(name, params):
    cards[name] = Card(name, params)

# Default Values for subjecctive Cards should be worst-case scenario?
# We need them even when calculationNeeded for non-recursive mode

#-------------Base--------------------

cardParams.reset()
cardParams.vp = botValue(1)
createCard('Estate', cardParams)

cardParams.reset()
cardParams.vp = botValue(3)
createCard('Duchy', cardParams)

cardParams.reset()
cardParams.vp = botValue(6)
createCard('Province', cardParams)

cardParams.reset()
cardParams.vp = botValue(-1)
createCard('Curse', cardParams)

cardParams.reset()
cardParams.money = botValue(1)
createCard('Copper', cardParams)

cardParams.reset()
cardParams.money = botValue(2)
createCard('Silver', cardParams)

cardParams.reset()
cardParams.money = botValue(3)
createCard('Gold', cardParams)

#-----------------Dominion---------------

cardParams.reset()
cardParams.draws = botValue(0, lambda: None, 'Depends on how many discards')
createCard('Cellar', cardParams)
# Incomplete - Discards

cardParams.reset()
cardParams.draws = botValue(2)
createCard('Moat', cardParams)
# Incomplete - defense

cardParams.reset()
cardParams.beneficial = botValue(False, lambda: None)
createCard('Chapel', cardParams)
# Incomplete - trashing

cardParams.reset()
cardParams.draws = botValue(1)
cardParams.actions = botValue(1)
createCard('Harbinger', cardParams)
# Incomplete - put on top

cardParams.reset()
cardParams.draws = botValue(1)
cardParams.actions = botValue(1)
cardParams.money = botValue(0, lambda: None, '0 normally, 1 if a silver is played')
createCard('Merchant', cardParams)
# Incomplete - extra money

cardParams.reset()
createCard('Workshop', cardParams)
# Incomplete - gain

cardParams.reset()
cardParams.draws = botValue(1)
cardParams.actions = botValue(2)
createCard('Village', cardParams)

cardParams.reset()
cardParams.money = botValue(2, lambda: None)
cardParams.actions = botValue(0, lambda: None, 'Worth 1 if it hits an action card')
cardParams.draws = botValue(0, lambda: None, 'Worth 1 if it hits an action card')
cardParams.buys = botValue(0, lambda: None)
cardParams.vp = botValue(0, lambda: None)
cardParams.cantrip = botValue(False, lambda: None)
createCard('Vassal', cardParams)
# Incomplete - uhhhh

cardParams.reset()
createCard('Bureaucrat', cardParams)
# Incomplete - gain silver to deck, attack

cardParams.reset()
cardParams.money = botValue(2)
createCard('Militia', cardParams)
# Incomplete - attack

cardParams.reset()
cardParams.vp = botValue(0, lambda: None, 'Varies with deck size', 100) # This should probably always be calculated. It's safe
createCard('Gardens', cardParams)
# Incomplete - vp calc

cardParams.reset()
cardParams.draws = botValue(3)
createCard('Smithy', cardParams)

cardParams.reset()
cardParams.money = botValue(0, lambda: None, 'Worth 3 if you trash a copper')
cardParams.beneficial = botValue(False, lambda: None)
createCard('Moneylender', cardParams)
# Incomplete - trashing, decision

cardParams.reset()
cardParams.beneficial = botValue(False, lambda: None)
createCard('Remodel', cardParams)
# Incomplete - gain, decision

cardParams.reset()
cardParams.money = botValue(0, lambda: None)
cardParams.actions = botValue(0, lambda: None, 'Worth 1 if you use it on an action (sort of)')
cardParams.draws = botValue(0, lambda: None)
cardParams.buys = botValue(0, True)
cardParams.vp = botValue(0, True)
cardParams.cantrip = botValue(False, True)
cardParams.beneficial = botValue(False, True)
createCard('Throne Room', cardParams)
# Incomplete - uhhhh

cardParams.reset()
cardParams.draws = botValue(1)
cardParams.actions = botValue(1)
cardParams.money = botValue(1)
createCard('Poacher', cardParams)
# Incomplete - discarding

cardParams.reset()
cardParams.draws = botValue(2)
cardParams.actions = botValue(1)
createCard('Laboratory', cardParams)


cardParams.reset()
cardParams.actions = botValue(2)
cardParams.money = botValue(2)
cardParams.buys = botValue(1)
createCard('Festival', cardParams)

cardParams.reset()
cardParams.money = botValue(1)
cardParams.draws = botValue(1)
cardParams.actions = botValue(1)
cardParams.buys = botValue(1)
createCard('Market', cardParams)

cardParams.reset()
createCard('Bandit', cardParams)
# Incomplete - gain gold, attack

cardParams.reset()
cardParams.money = botValue(1, lambda: None, 'Only worth 1 if you have an upgradable treasure', 100)
createCard('Mine', cardParams)
# Incomplete - trash, beneficial???

cardParams.reset()
cardParams.draws = botValue(4)
cardParams.buys = botValue(1)
createCard('Council Room', cardParams)
# Incomplete - Opponent Gain

cardParams.reset()
cardParams.draws = botValue(1)
cardParams.actions = botValue(1)
createCard('Sentry', cardParams)
# Incomplete - trashing/discarding/ordering

cardParams.reset()
cardParams.draws = botValue(3, lambda: None, 'Draws up to 7')
createCard('Library', cardParams)
# Incomplete - drawing, discarding?

cardParams.reset()
cardParams.draws = botValue(2)
createCard('Witch', cardParams)
# Incomplete - attack

cardParams.reset()
createCard('Artisan', cardParams)
# Incomplete - gain to hand

def getCard(name):
    if name not in cards:
        logError('name \'%s\' not found' % name)
    return cards[name]

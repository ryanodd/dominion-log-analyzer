from utils.log import logError
from bot.botTypes import botValue
from game.card.gCardFactory import getCard
from game.card.gCard import CardType

# Used as just a parameter for constructing actual CardInfos.
# This makes it easy to write CardInfos for every card in the game (less writing)
class CardInfoParams:
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

# This class makes card-agnostic algorithms possible. I'm down to rename it
class CardInfo:
    def __init__(self, name, cardInfoParams):
        self.name = name

        self.money = cardInfoParams.money
        self.draws = cardInfoParams.draws
        self.actions = cardInfoParams.actions
        self.buys = cardInfoParams.buys
        self.vp = cardInfoParams.vp

        # Funny one. Used for bot logic only
        self.beneficial = cardInfoParams.beneficial

        # Careful with these defaults. Not sure about them. Can have card-for-card overriding or one universal alg hmmmmm
        self.cantrip = botValue(False, (self.draws.value > 0 and self.actions.value > 0 ))
        self.extraDraws = botValue(max(0, self.draws.value - 1), self.draws.evaluator, self.draws.message, self.draws.importance)
        self.extraActions = botValue(max(0, self.actions.value - 1), self.actions.evaluator, self.actions.message, self.actions.importance)
        self.terminal = botValue(CardType.ACTION in getCard(self.name).types and self.actions.value == 0)
        self.stop = botValue(self.draws.value == 0)

# Maps card names to CardInfo objects
info = {}
cardInfoParams = CardInfoParams()

def createCardInfo(name, params):
    info[name] = CardInfo(name, params)

# Default Values for subjecctive Cards should be worst-case scenario?
# We need them even when calculationNeeded for non-recursive mode

#-------------Base--------------------

cardInfoParams.reset()
cardInfoParams.vp = botValue(1)
createCardInfo('Estate', cardInfoParams)

cardInfoParams.reset()
cardInfoParams.vp = botValue(3)
createCardInfo('Duchy', cardInfoParams)

cardInfoParams.reset()
cardInfoParams.vp = botValue(6)
createCardInfo('Province', cardInfoParams)

cardInfoParams.reset()
cardInfoParams.vp = botValue(-1)
createCardInfo('Curse', cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = botValue(1)
createCardInfo('Copper', cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = botValue(2)
createCardInfo('Silver', cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = botValue(3)
createCardInfo('Gold', cardInfoParams)

#-----------------Dominion---------------

cardInfoParams.reset()
cardInfoParams.draws = botValue(0, lambda: None, 'Depends on how many discards')
createCardInfo('Cellar', cardInfoParams)
# Incomplete - Discards

cardInfoParams.reset()
cardInfoParams.draws = botValue(2)
createCardInfo('Moat', cardInfoParams)
# Incomplete - defense

cardInfoParams.reset()
cardInfoParams.beneficial = botValue(False, lambda: None)
createCardInfo('Chapel', cardInfoParams)
# Incomplete - trashing

cardInfoParams.reset()
cardInfoParams.draws = botValue(1)
cardInfoParams.actions = botValue(1)
createCardInfo('Harbinger', cardInfoParams)
# Incomplete - put on top

cardInfoParams.reset()
cardInfoParams.draws = botValue(1)
cardInfoParams.actions = botValue(1)
cardInfoParams.money = botValue(0, lambda: None, '0 normally, 1 if a silver is played')
createCardInfo('Merchant', cardInfoParams)
# Incomplete - extra money

cardInfoParams.reset()
createCardInfo('Workshop', cardInfoParams)
# Incomplete - gain

cardInfoParams.reset()
cardInfoParams.draws = botValue(1)
cardInfoParams.actions = botValue(2)
createCardInfo('Village', cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = botValue(2, lambda: None)
cardInfoParams.actions = botValue(0, lambda: None, 'Worth 1 if it hits an action card')
cardInfoParams.draws = botValue(0, lambda: None, 'Worth 1 if it hits an action card')
cardInfoParams.buys = botValue(0, lambda: None)
cardInfoParams.vp = botValue(0, lambda: None)
cardInfoParams.cantrip = botValue(False, lambda: None)
createCardInfo('Vassal', cardInfoParams)
# Incomplete - uhhhh

cardInfoParams.reset()
createCardInfo('Bureaucrat', cardInfoParams)
# Incomplete - gain silver to deck, attack

cardInfoParams.reset()
cardInfoParams.money = botValue(2)
createCardInfo('Militia', cardInfoParams)
# Incomplete - attack

cardInfoParams.reset()
cardInfoParams.vp = botValue(0, lambda: None, 'Varies with deck size', 100) # This should probably always be calculated. It's safe
createCardInfo('Gardens', cardInfoParams)
# Incomplete - vp calc

cardInfoParams.reset()
cardInfoParams.draws = botValue(3)
createCardInfo('Smithy', cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = botValue(0, lambda: None, 'Worth 3 if you trash a copper')
cardInfoParams.beneficial = botValue(False, lambda: None)
createCardInfo('Moneylender', cardInfoParams)
# Incomplete - trashing, decision

cardInfoParams.reset()
cardInfoParams.beneficial = botValue(False, lambda: None)
createCardInfo('Remodel', cardInfoParams)
# Incomplete - gain, decision

cardInfoParams.reset()
cardInfoParams.money = botValue(0, lambda: None)
cardInfoParams.actions = botValue(0, lambda: None, 'Worth 1 if you use it on an action (sort of)')
cardInfoParams.draws = botValue(0, lambda: None)
cardInfoParams.buys = botValue(0, True)
cardInfoParams.vp = botValue(0, True)
cardInfoParams.cantrip = botValue(False, True)
cardInfoParams.beneficial = botValue(False, True)
createCardInfo('Throne Room', cardInfoParams)
# Incomplete - uhhhh

cardInfoParams.reset()
cardInfoParams.draws = botValue(1)
cardInfoParams.actions = botValue(1)
cardInfoParams.money = botValue(1)
createCardInfo('Poacher', cardInfoParams)
# Incomplete - discarding

cardInfoParams.reset()
cardInfoParams.draws = botValue(2)
cardInfoParams.actions = botValue(1)
createCardInfo('Laboratory', cardInfoParams)


cardInfoParams.reset()
cardInfoParams.actions = botValue(2)
cardInfoParams.money = botValue(2)
cardInfoParams.buys = botValue(1)
createCardInfo('Festival', cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = botValue(1)
cardInfoParams.draws = botValue(1)
cardInfoParams.actions = botValue(1)
cardInfoParams.buys = botValue(1)
createCardInfo('Market', cardInfoParams)

cardInfoParams.reset()
createCardInfo('Bandit', cardInfoParams)
# Incomplete - gain gold, attack

cardInfoParams.reset()
cardInfoParams.money = botValue(1, lambda: None, 'Only worth 1 if you have an upgradable treasure', 100)
createCardInfo('Mine', cardInfoParams)
# Incomplete - trash, beneficial???

cardInfoParams.reset()
cardInfoParams.draws = botValue(4)
cardInfoParams.buys = botValue(1)
createCardInfo('Council Room', cardInfoParams)
# Incomplete - Opponent Gain

cardInfoParams.reset()
cardInfoParams.draws = botValue(1)
cardInfoParams.actions = botValue(1)
createCardInfo('Sentry', cardInfoParams)
# Incomplete - trashing/discarding/ordering

cardInfoParams.reset()
cardInfoParams.draws = botValue(3, lambda: None, 'Draws up to 7')
createCardInfo('Library', cardInfoParams)
# Incomplete - drawing, discarding?

cardInfoParams.reset()
cardInfoParams.draws = botValue(2)
createCardInfo('Witch', cardInfoParams)
# Incomplete - attack

cardInfoParams.reset()
createCardInfo('Artisan', cardInfoParams)
# Incomplete - gain to hand

def getCardInfo(name):
    if name not in info:
        logError('name \'%s\' not found' % name)
    return info[name]

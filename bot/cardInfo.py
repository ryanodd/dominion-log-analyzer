from utils.log import logError
from bot.botTypes import botValue

# Used as just a parameter for constructing actual CardInfos.
# This makes it easy to write CardInfos for every card in the game (less writing)
class CardInfoParams:
    def __init__(self):
        self.money = botValue(0)
        self.draws = botValue(0)
        self.actions = botValue(0)
        self.buys = botValue(0)
        self.vp = botValue(0)

        # Careful with these defaults. Not sure about them. Can have card-for-card overriding or one universal alg hmmmmm
        self.cantrip = botValue(False, (self.draws.value > 0 and self.actions.value > 0 ))
        self.extraDraws = botValue(max(0, self.draws.value - 1), self.draws.evaluator, self.draws.message, self.draws.importance)
        self.extraActions = botValue(max(0, self.actions.value - 1), self.actions.evaluator, self.actions.message, self.actions.importance)
        self.terminal = botValue(self.actions == 0)
        self.stop = botValue(self.draws == 0)
        self.beneficial = botValue(True)

    # Woah. I wonder if this is good or bad. memory & performance
    def reset(self):
        self.__init__()

# This class makes card-agnostic algorithms possible. I'm down to rename it
class CardInfo:
    def __init__(self, cardInfoParams):
        self.money = cardInfoParams.money
        self.draws = cardInfoParams.draws
        self.actions = cardInfoParams.actions
        self.buys = cardInfoParams.buys
        self.vp = cardInfoParams.vp

        self.cantrip = cardInfoParams.cantrip
        self.extraDraws = cardInfoParams.extraDraws
        self.extraActions = cardInfoParams.extraActions
        self.terminal = cardInfoParams.terminal
        self.stop = cardInfoParams.stop
        self.beneficial = cardInfoParams.beneficial

# Maps card names to CardInfo objects
info = {}
cardInfoParams = CardInfoParams()

# Default Values for subjecctive Cards should be worst-case scenario?
# We need them even when calculationNeeded for non-recursive mode

#-------------Base--------------------

cardInfoParams.reset()
cardInfoParams.vp = botValue(1)
info['Estate'] = CardInfo(CardInfoParams())

cardInfoParams.reset()
cardInfoParams.vp = botValue(3)
info['Duchy'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.vp = botValue(6)
info['Province'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.vp = botValue(-1)
info['Curse'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = botValue(1)
info['Copper'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = botValue(2)
info['Silver'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = botValue(3)
info['Gold'] = CardInfo(cardInfoParams)

#-----------------Dominion---------------

cardInfoParams.reset()
cardInfoParams.draws = botValue(0, lambda: None, 'Depends on how many discards')
info['Cellar'] = CardInfo(cardInfoParams)
# Incomplete - Discards

cardInfoParams.reset()
cardInfoParams.draws = botValue(2)
info['Moat'] = CardInfo(cardInfoParams)
# Incomplete - defense

cardInfoParams.reset()
cardInfoParams.beneficial = botValue(False, lambda: None)
info['Chapel'] = CardInfo(cardInfoParams)
# Incomplete - trashing

cardInfoParams.reset()
cardInfoParams.draws = botValue(1)
cardInfoParams.actions = botValue(1)
info['Harbinger'] = CardInfo(cardInfoParams)
# Incomplete - put on top

cardInfoParams.reset()
cardInfoParams.draws = botValue(1)
cardInfoParams.actions = botValue(1)
cardInfoParams.money = botValue(0, lambda: None, '0 normally, 1 if a silver is played')
info['Merchant'] = CardInfo(cardInfoParams)
# Incomplete - extra money

cardInfoParams.reset()
info['Workshop'] = CardInfo(cardInfoParams)
# Incomplete - gain

cardInfoParams.reset()
cardInfoParams.draws = botValue(1)
cardInfoParams.actions = botValue(2)
info['Village'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = botValue(2, lambda: None)
cardInfoParams.actions = botValue(0, lambda: None, 'Worth 1 if it hits an action card')
cardInfoParams.draws = botValue(0, lambda: None, 'Worth 1 if it hits an action card')
cardInfoParams.buys = botValue(0, lambda: None)
cardInfoParams.vp = botValue(0, lambda: None)
cardInfoParams.cantrip = botValue(False, lambda: None)
info['Vassal'] = CardInfo(cardInfoParams)
# Incomplete - uhhhh

cardInfoParams.reset()
info['Bureaucrat'] = CardInfo(cardInfoParams)
# Incomplete - gain silver to deck, attack

cardInfoParams.reset()
cardInfoParams.money = botValue(2)
info['Militia'] = CardInfo(cardInfoParams)
# Incomplete - attack

cardInfoParams.reset()
cardInfoParams.vp = botValue(0, lambda: None, 'Varies with deck size', 100) # This should probably always be calculated. It's safe
info['Gardens'] = CardInfo(cardInfoParams)
# Incomplete - vp calc

cardInfoParams.reset()
cardInfoParams.draws = botValue(3)
info['Smithy'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = botValue(0, lambda: None, 'Worth 3 if you trash a copper')
cardInfoParams.beneficial = botValue(False, lambda: None)
info['Moneylender'] = CardInfo(cardInfoParams)
# Incomplete - trashing, decision

cardInfoParams.reset()
cardInfoParams.beneficial = botValue(False, lambda: None)
info['Remodel'] = CardInfo(cardInfoParams)
# Incomplete - gain, decision

cardInfoParams.reset()
cardInfoParams.money = botValue(0, lambda: None)
cardInfoParams.actions = botValue(0, lambda: None, 'Worth 1 if you use it on an action (sort of)')
cardInfoParams.draws = botValue(0, lambda: None)
cardInfoParams.buys = botValue(0, True)
cardInfoParams.vp = botValue(0, True)
cardInfoParams.cantrip = botValue(False, True)
cardInfoParams.beneficial = botValue(False, True)
info['Throne Room'] = CardInfo(cardInfoParams)
# Incomplete - uhhhh

cardInfoParams.reset()
cardInfoParams.draws = botValue(1)
cardInfoParams.actions = botValue(1)
cardInfoParams.money = botValue(1)
info['Poacher'] = CardInfo(cardInfoParams)
# Incomplete - discarding

cardInfoParams.reset()
cardInfoParams.draws = botValue(2)
cardInfoParams.actions = botValue(1)
info['Laboratory'] = CardInfo(cardInfoParams)


cardInfoParams.reset()
cardInfoParams.actions = botValue(2)
cardInfoParams.money = botValue(2)
cardInfoParams.buys = botValue(1)
info['Festival'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = botValue(1)
cardInfoParams.draws = botValue(1)
cardInfoParams.actions = botValue(1)
cardInfoParams.buys = botValue(1)
info['Market'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
info['Bandit'] = CardInfo(cardInfoParams)
# Incomplete - gain gold, attack

cardInfoParams.reset()
cardInfoParams.money = botValue(1, lambda: None, 'Only worth 1 if you have an upgradable treasure', 100)
info['Mine'] = CardInfo(cardInfoParams)
# Incomplete - trash, beneficial???

cardInfoParams.reset()
cardInfoParams.draws = botValue(4)
cardInfoParams.buys = botValue(1)
info['Council Room'] = CardInfo(cardInfoParams)
# Incomplete - Opponent Gain

cardInfoParams.reset()
cardInfoParams.draws = botValue(1)
cardInfoParams.actions = botValue(1)
info['Sentry'] = CardInfo(cardInfoParams)
# Incomplete - trashing/discarding/ordering

cardInfoParams.reset()
cardInfoParams.draws = botValue(2, lambda: None, 'Draws up to 7')
info['Library'] = CardInfo(cardInfoParams)
# Incomplete - drawing, discarding?

cardInfoParams.reset()
cardInfoParams.draws = botValue(2)
info['Witch'] = CardInfo(cardInfoParams)
# Incomplete - attack

cardInfoParams.reset()
info['Artisan'] = CardInfo(cardInfoParams)
# Incomplete - gain to hand

def getCardInfo(name):
    if name not in info:
        logError('name \'%s\' not found' % name)
    return info[name]

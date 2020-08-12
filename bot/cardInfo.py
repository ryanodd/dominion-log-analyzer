from utils.log import logError
from bot.botTypes import botValue

class CardInfoParams:
    def __init__(self):
        self.money = botValue(0)
        self.draws = botValue(0)
        self.actions = botValue(0)
        self.buys = botValue(0)
        self.vp = botValue(0)

        # Careful with these defaults. Not sure about them. Can have card-for-card overriding or one universal alg hmmmmm
        self.cantrip = botValue(False, (self.draws.value > 0 and self.actions.value > 0 ))
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
cardInfoParams.draws = botValue(1, None)
info['Cellar'] = CardInfo(cardInfoParams)
# Incomplete - Discards

cardInfoParams.reset()
cardInfoParams.draws = botValue(2)
info['Moat'] = CardInfo(cardInfoParams)
# Incomplete - defense

cardInfoParams.reset()
cardInfoParams.beneficial = botValue(False, None)
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
cardInfoParams.money = botValue(0, None)
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
cardInfoParams.money = botValue(2, None)
cardInfoParams.actions = botValue(0, None)
cardInfoParams.draws = botValue(0, None)
cardInfoParams.buys = botValue(0, None)
cardInfoParams.vp = botValue(0, None)
cardInfoParams.cantrip = botValue(False, None)
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
cardInfoParams.vp = botValue(0, None, 100)
info['Gardens'] = CardInfo(cardInfoParams)
# Incomplete - vp calc

cardInfoParams.reset()
cardInfoParams.draws = botValue(3)
info['Smithy'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = botValue(0, None)
cardInfoParams.beneficial = botValue(False, None)
info['Moneylender'] = CardInfo(cardInfoParams)
# Incomplete - trashing, decision

cardInfoParams.reset()
cardInfoParams.beneficial = botValue(False, None)
info['Remodel'] = CardInfo(cardInfoParams)
# Incomplete - gain, decision

cardInfoParams.reset()
cardInfoParams.money = botValue(0, None)
cardInfoParams.actions = botValue(0, None)
cardInfoParams.draws = botValue(0, None)
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
cardInfoParams.money = botValue(0, None, 100)
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
cardInfoParams.draws = botValue(0, None)
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

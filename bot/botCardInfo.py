from utils.log import logError

class CardInfoValue:
    def __init__(self, value, calculationNeeded=False, subjective=False):
        self.value = value
        self.calculationNeeded = calculationNeeded
        self.subjective = subjective


class CardInfoParams:
    def __init__(self):
        self.money = CardInfoValue(0)
        self.draws = CardInfoValue(0)
        self.actions = CardInfoValue(0)
        self.buys = CardInfoValue(0)
        self.vp = CardInfoValue(0)

        # Careful with this default. Not sure about it
        self.cantrip = CardInfoValue((self.draws > 0 and self.actions > 0 ))
        self.beneficial = CardInfoValue(True)

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

# Default Values for subjecctive Cards should be worst-case scenario. Hopefully that's always a thing.
# We need them even when calculationNeeded for non-recursive mode

#-------------Base--------------------

cardInfoParams.reset()
cardInfoParams.vp = CardInfoValue(1)
info['Estate'] = CardInfo(CardInfoParams())

cardInfoParams.reset()
cardInfoParams.vp = CardInfoValue(3)
info['Duchy'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.vp = CardInfoValue(6)
info['Province'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.vp = CardInfoValue(-1)
info['Curse'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = CardInfoValue(1)
info['Copper'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = CardInfoValue(2)
info['Silver'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = CardInfoValue(3)
info['Gold'] = CardInfo(cardInfoParams)

#-----------------Dominion---------------

cardInfoParams.reset()
cardInfoParams.draws = CardInfoValue(1, True, True)
info['Cellar'] = CardInfo(cardInfoParams)
# Incomplete - Discards

cardInfoParams.reset()
cardInfoParams.draws = CardInfoValue(2)
info['Moat'] = CardInfo(cardInfoParams)
# Incomplete - defense

cardInfoParams.reset()
cardInfoParams.beneficial = CardInfoValue(False, True, True)
info['Chapel'] = CardInfo(cardInfoParams)
# Incomplete - trashing

cardInfoParams.reset()
cardInfoParams.draws = CardInfoValue(1)
cardInfoParams.actions = CardInfoValue(1)
info['Harbinger'] = CardInfo(cardInfoParams)
# Incomplete - put on top

cardInfoParams.reset()
cardInfoParams.draws = CardInfoValue(1)
cardInfoParams.actions = CardInfoValue(1)
cardInfoParams.money = CardInfoValue(0, True, True)
info['Merchant'] = CardInfo(cardInfoParams)
# Incomplete - extra money

cardInfoParams.reset()
info['Workshop'] = CardInfo(cardInfoParams)
# Incomplete - gain

cardInfoParams.reset()
cardInfoParams.draws = CardInfoValue(1)
cardInfoParams.actions = CardInfoValue(2)
info['Village'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = CardInfoParams(2, True, True)
cardInfoParams.actions = CardInfoParams(0, True, True)
cardInfoParams.draws = CardInfoParams(0, True, True)
cardInfoParams.buys = CardInfoParams(0, True, True)
cardInfoParams.vp = CardInfoParams(0, True, True)
cardInfoParams.cantrip(False, True, True)
info['Vassal'] = CardInfo(cardInfoParams)
# Incomplete - uhhhh

cardInfoParams.reset()
info['Bureaucrat'] = CardInfo(cardInfoParams)
# Incomplete - gain silver to deck, attack

cardInfoParams.reset()
cardInfoParams.money = CardInfoValue(2)
info['Militia'] = CardInfo(cardInfoParams)
# Incomplete - attack

cardInfoParams.reset()
cardInfoParams.vp = CardInfoValue(0, True)
info['Gardens'] = CardInfo(cardInfoParams)
# Incomplete - vp calc

cardInfoParams.reset()
cardInfoParams.draws = CardInfoValue(3)
info['Smithy'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = CardInfoValue(0, True, True)
cardInfoParams.beneficial = CardInfoValue(False, True, True)
info['Moneylender'] = CardInfo(cardInfoParams)
# Incomplete - trashing, decision

cardInfoParams.reset()
cardInfoParams.beneficial = CardInfoValue(False, True, True)
info['Remodel'] = CardInfo(cardInfoParams)
# Incomplete - gain, decision

cardInfoParams.reset()
cardInfoParams.money = CardInfoParams(0, True, True)
cardInfoParams.actions = CardInfoParams(0, True, True)
cardInfoParams.draws = CardInfoParams(0, True, True)
cardInfoParams.buys = CardInfoParams(0, True, True)
cardInfoParams.vp = CardInfoParams(0, True, True)
cardInfoParams.cantrip(False, True, True)
cardInfoParams.beneficial(False, True, True)
info['Throne Room'] = CardInfo(cardInfoParams)
# Incomplete - uhhhh

cardInfoParams.reset()
cardInfoParams.draws = CardInfoValue(1)
cardInfoParams.actions = CardInfoValue(1)
cardInfoParams.money = CardInfoValue(1)
info['Poacher'] = CardInfo(cardInfoParams)
# Incomplete - discarding

cardInfoParams.reset()
cardInfoParams.draws = CardInfoValue(2)
cardInfoParams.actions = CardInfoValue(1)
info['Laboratory'] = CardInfo(cardInfoParams)


cardInfoParams.reset()
cardInfoParams.actions = CardInfoValue(2)
cardInfoParams.money = CardInfoValue(2)
cardInfoParams.buys = CardInfoValue(1)
info['Festival'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = CardInfoValue(1)
cardInfoParams.draws = CardInfoValue(1)
cardInfoParams.actions = CardInfoValue(1)
cardInfoParams.buys = CardInfoValue(1)
info['Market'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
info['Bandit'] = CardInfo(cardInfoParams)
# Incomplete - gain gold, attack

cardInfoParams.reset()
cardInfoParams.money = CardInfoValue(0, True, True)
info['Mine'] = CardInfo(cardInfoParams)
# Incomplete - trash, beneficial???

cardInfoParams.reset()
cardInfoParams.draws = CardInfoValue(4)
cardInfoParams.buys = CardInfoValue(1)
info['Council Room'] = CardInfo(cardInfoParams)
# Incomplete - Opponent Gain

cardInfoParams.reset()
cardInfoParams.draws = CardInfoValue(1)
cardInfoParams.actions = CardInfoValue(1)
info['Sentry'] = CardInfo(cardInfoParams)
# Incomplete - trashing/discarding/ordering

cardInfoParams.reset()
cardInfoParams.draws = CardInfoValue(0, True, True)
info['Library'] = CardInfo(cardInfoParams)
# Incomplete - drawing, discarding?

cardInfoParams.reset()
cardInfoParams.draws = CardInfoValue(2)
info['Witch'] = CardInfo(cardInfoParams)
# Incomplete - attack

cardInfoParams.reset()
info['Artisan'] = CardInfo(cardInfoParams)
# Incomplete - gain to hand


def getCardInfo(name):
    if name not in info:
        logError('name \'%s\' not found' % name)
    return info[name]

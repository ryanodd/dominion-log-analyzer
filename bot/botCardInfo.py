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

# Maps card names to CardInfo objects
info = {}
cardInfoParams = CardInfoParams()

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

cardInfoParams.reset()
info['Chapel'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.actions = CardInfoValue(2)
cardInfoParams.money = CardInfoValue(2)
cardInfoParams.buys = CardInfoValue(1)
info['Festival'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.vp = CardInfoValue(0, True)
info['Gardens'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.draws = CardInfoValue(2)
cardInfoParams.actions = CardInfoValue(1)
info['Laboratory'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.money = CardInfoValue(1)
cardInfoParams.draws = CardInfoValue(1)
cardInfoParams.actions = CardInfoValue(1)
cardInfoParams.buys = CardInfoValue(1)
info['Market'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.draws = CardInfoValue(3)
info['Smithy'] = CardInfo(cardInfoParams)

cardInfoParams.reset()
cardInfoParams.draws = CardInfoValue(1)
cardInfoParams.actions = CardInfoValue(2)
info['Village'] = CardInfo(cardInfoParams)


def getCardInfo(name):
    if name not in info:
        logError('name \'%s\' not found' % name)
    return info[name]

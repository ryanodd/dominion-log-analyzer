
# This class makes card-agnostic algorithms possible. I'm down to rename it
class CardInfo:
    def __init__(self, money=0, draws=0, actions=0, buys=0, vp=0):
        self.money = money
        self.draws = draws
        self.actions = actions
        self.buys = buys
        self.vp = vp


# Maps card names to CardInfo objects
info = {}

info['Estate'] = CardInfo(vp=1)
info['Duchy'] = CardInfo(vp=3)
info['Province'] = CardInfo(vp=6)
info['Curse'] = CardInfo(vp=-1)
info['Copper'] = CardInfo(money=1)
info['Silver'] = CardInfo(money=2)
info['Gold'] = CardInfo(money=3)

info['Festival'] = CardInfo(money=2, buys=1)
info['Gardens'] = CardInfo(vp=3) # wrong for now. Where should the math be done?
info['Laboratory'] = CardInfo(draws=2, actions=1)
info['Market'] = CardInfo(money=1, draws=1, actions=1, buys=1)
info['Smithy'] = CardInfo(draws=3)
info['Village'] = CardInfo(draws=1, actions=2)


def getCardInfo(name):
    if name not in info:
        logError('name \'%s\' not found' % name)
    return info[name]

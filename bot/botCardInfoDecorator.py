from bot.botCardInfo import getCardInfo
import copy

# Wraps objectiveCardInfo
class BotCardInfoDecorator:
    def __init__(self):
        self.moneyFunction = {}
        self.drawsFunction = {}
        self.actionsFunction = {}
        self.buysFunction = {}
        self.vpFunction = {}
    
    def getCardInfo(self, name, deck):
        objectiveInfo = getCardInfo(name)
        returnInfo = copy.copy(objectiveInfo)
        if (self.moneyFunction[name]):
            returnInfo.money = self.moneyFunction[name](deck)
        if (self.drawsFunction[name]):
            returnInfo.draws = self.drawsFunction[name](deck)
        if (self.actionsFunction[name]):
            returnInfo.actions = self.actionsFunction[name](deck)
        if (self.buysFunction[name]):
            returnInfo.buys = self.buysFunction[name](deck)
        if (self.vpFunction[name]):
            returnInfo.vp = self.vpFunction[name](deck)
        return returnInfo
        
    def assignMoneyFunction(self, name, moneyFunction):
        self.moneyFunction[name] = moneyFunction
    def assignDrawsFunction(self, name, drawsFunction):
        self.drawsFunction[name] = drawsFunction
    def assignActionsFunction(self, name, actionsFunction):
        self.actionsFunction[name] = actionsFunction
    def assignBuysFunction(self, name, buysFunction):
        self.buysFunction[name] = buysFunction
    def assignVPFunction(self, name, vpFunction):
        self.vpFunction[name] = vpFunction
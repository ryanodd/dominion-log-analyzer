from objectiveCardInfo import getInfo
import copy

# Wraps objectiveCardInfo
class BotCardInfoDecorator:
    def __init__(self):
        self.moneyFunction = {}
        self.drawsFunction = {}
        self.actionsFunction = {}
        self.buysFunction = {}
        self.vpFunction = {}
    
    def getInfo(name, deck):
        objectiveInfo = getInfo(name)
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
        
    def assignMoneyFunction(name, moneyFunction):
        self.moneyFunction[name] = moneyFunction
    def assignDrawsFunction(name, drawsFunction):
        self.drawsFunction[name] = drawsFunction
    def assignActionsFunction(name, actionsFunction):
        self.actionsFunction[name] = actionsFunction
    def assignBuysFunction(name, buysFunction):
        self.buysFunction[name] = buysFunction
    def assignVPFunction(name, vpFunction):
        self.vpFunction[name] = vpFunction
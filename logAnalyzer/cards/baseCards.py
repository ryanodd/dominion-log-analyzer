
#-------------Base Cards--------------------

from utils.log import logError 
from logAnalyzer.logAnalyzerTypes import CardValue
from logAnalyzer.card import Card, CardParams

# Maps card names to Card constructors
cardFns = {}

def create_Estate():
    cardParams = CardParams()
    cardParams.isVictory = CardValue(True)
    cardParams.cost = CardValue(2)
    cardParams.vp = CardValue(1)
    return cardParams
cardFns['Estate'] = create_Estate

def create_Duchy():
    cardParams = CardParams()
    cardParams.isVictory = CardValue(True)
    cardParams.cost = CardValue(5)
    cardParams.vp = CardValue(3)
    return cardParams
cardFns['Duchy'] = create_Duchy

def create_Province():
    cardParams = CardParams()
    cardParams.isVictory = CardValue(True)
    cardParams.cost = CardValue(8)
    cardParams.vp = CardValue(6)
    return cardParams
cardFns['Province'] = create_Province

def create_Curse():
    cardParams = CardParams()
    cardParams.isCurse = CardValue(True)
    cardParams.cost = CardValue(0)
    cardParams.vp = CardValue(-1)
    return cardParams
cardFns['Curse'] = create_Curse

def create_Copper():
    cardParams = CardParams()
    cardParams.isTreasure = CardValue(True)
    cardParams.cost = CardValue(0)
    cardParams.money = CardValue(1)
    return cardParams
cardFns['Copper'] = create_Copper

def create_Silver():
    cardParams = CardParams()
    cardParams.isTreasure = CardValue(True)
    cardParams.cost = CardValue(3)
    cardParams.money = CardValue(2)
    return cardParams
cardFns['Silver'] = create_Silver

def create_Gold():
    cardParams = CardParams()
    cardParams.isTreasure = CardValue(True)
    cardParams.cost = CardValue(6)
    cardParams.money = CardValue(3)
    return cardParams
cardFns['Gold'] = create_Gold

def getBaseCardFns():
  return cardFns

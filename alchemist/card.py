import math

from utils.log import logError
from alchemist.botTypes import botValue

# Used as just a parameter for constructing actual Cards.
# This makes it easy to implement every card in the game (more defaults, less writing)
# The Card fields not included in CardParams are generated from the given params.
class CardParams:
    def __init__(self):
        self.isAction = botValue(False)
        self.isTreasure = botValue(False)
        self.isVictory = botValue(False)
        self.isCurse = botValue(False)
        self.isAttack = botValue(False)
        self.isReaction = botValue(False)
        self.isDuration = botValue(False)
        self.isReserve = botValue(False)
        self.isNight = botValue(False)

        self.cost = botValue(0)
        self.potionCost = botValue(0) # or bool maybe?
        self.debtCost = botValue(0)

        self.money = botValue(0)
        self.draws = botValue(0)
        self.actions = botValue(0)
        self.buys = botValue(0)
        self.vp = botValue(0)

        self.discards = botValue(0)

        self.doesGain = botValue(False)
        self.doesTrash = botValue(False)
        self.doesSift = botValue(False)

        self.beneficial = botValue(True)

    # Woah. I wonder if this is good or bad. memory & performance
    def reset(self):
        self.__init__()

class Card:
    def __init__(self, name, cardParams):
        self.name = name
    
        self.isAction = cardParams.isAction
        self.isTreasure = cardParams.isTreasure
        self.isVictory = cardParams.isVictory
        self.isCurse = cardParams.isCurse
        self.isAttack = cardParams.isAttack
        self.isReaction = cardParams.isReaction
        self.isDuration = cardParams.isDuration
        self.isReserve = cardParams.isReserve
        self.isNight = cardParams.isNight

        self.cost = cardParams.cost
        self.potionCost = cardParams.potionCost
        self.debtCost = cardParams.debtCost
        
        self.money = cardParams.money
        self.draws = cardParams.draws
        self.actions = cardParams.actions
        self.buys = cardParams.buys
        self.vp = cardParams.vp

        self.discards = cardParams.discards

        self.doesGain = cardParams.doesGain
        self.doesTrash = cardParams.doesTrash

        # Funny one. Used for bot logic only
        self.beneficial = cardParams.beneficial

        # Careful with these defaults. Not sure about them. Can have card-for-card overriding or one universal alg hmmmmm
        self.cantrip = botValue(False, (self.draws.value > 0 and self.actions.value > 0 ))
        self.extraDraws = botValue(max(0, self.draws.value - 1), self.draws.evaluator, self.draws.message, self.draws.importance)
        self.extraActions = botValue(max(0, self.actions.value - 1), self.actions.evaluator, self.actions.message, self.actions.importance)
        self.terminal = botValue(self.isAction.value and self.actions.value == 0)
        self.stop = botValue(self.draws.value == 0)

# Maps card names to Card objects
cardFns = {}

# Default Values for subjective Cards should be worst-case scenario?
# We need them even when calculationNeeded for non-recursive mode

#-------------Base--------------------

def create_Estate():
    cardParams = CardParams()
    cardParams.isVictory = botValue(True)
    cardParams.cost = botValue(2)
    cardParams.vp = botValue(1)
    return cardParams
cardFns['Estate'] = create_Estate

def create_Duchy():
    cardParams = CardParams()
    cardParams.isVictory = botValue(True)
    cardParams.cost = botValue(5)
    cardParams.vp = botValue(3)
    return cardParams
cardFns['Duchy'] = create_Duchy

def create_Province():
    cardParams = CardParams()
    cardParams.isVictory = botValue(True)
    cardParams.cost = botValue(8)
    cardParams.vp = botValue(6)
    return cardParams
cardFns['Province'] = create_Province

def create_Curse():
    cardParams = CardParams()
    cardParams.isCurse = botValue(True)
    cardParams.cost = botValue(0)
    cardParams.vp = botValue(-1)
    return cardParams
cardFns['Curse'] = create_Curse

def create_Copper():
    cardParams = CardParams()
    cardParams.isTreasure = botValue(True)
    cardParams.cost = botValue(0)
    cardParams.money = botValue(1)
    return cardParams
cardFns['Copper'] = create_Copper

def create_Silver():
    cardParams = CardParams()
    cardParams.isTreasure = botValue(True)
    cardParams.cost = botValue(3)
    cardParams.money = botValue(2)
    return cardParams
cardFns['Silver'] = create_Silver

def create_Gold():
    cardParams = CardParams()
    cardParams.isTreasure = botValue(True)
    cardParams.cost = botValue(6)
    cardParams.money = botValue(3)
    return cardParams
cardFns['Gold'] = create_Gold

#-----------------Dominion---------------

def create_Cellar(numDiscards=None):
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(2)
    if numDiscards is None:
        cardParams.discards = botValue(0, lambda: None, 'Depends on how many discards')
        cardParams.draws = botValue(0, lambda: None, 'Depends on how many discards')
    elif numDiscards is not None:
        cardParams.discards = botValue(numDiscards)
        cardParams.draws = botValue(numDiscards)
    return cardParams
cardFns['Cellar'] = create_Cellar

def create_Moat():
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.isReaction = botValue(True)
    cardParams.cost = botValue(2)
    cardParams.draws = botValue(2)
    return cardParams
cardFns['Moat'] = create_Moat
# Incomplete - defense

def create_Chapel():
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(2)
    cardParams.doesTrash = botValue(True)
    cardParams.beneficial = botValue(False, lambda: None) # funy
    return cardParams
cardFns['Chapel'] = create_Chapel

def create_Harbinger():
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(3)
    cardParams.draws = botValue(1)
    cardParams.actions = botValue(1)
    return cardParams
cardFns['Harbinger'] = create_Harbinger
# Incomplete - put on top

def create_Merchant(playsSilver=None):
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(3)
    cardParams.draws = botValue(1)
    cardParams.actions = botValue(1)

    if playsSilver is None:
        cardParams.money = botValue(0, lambda: None, '0 normally, 1 if a silver is played')
    elif playsSilver:
        cardParams.money = botValue(1)
    elif not playsSilver:
        cardParams.money = botValue(0)

    return cardParams
cardFns['Merchant'] = create_Merchant

def create_Workshop():
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(3)
    cardParams.doesGain = botValue(True)
    return cardParams
cardFns['Workshop'] = create_Workshop

def create_Village():
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(3)
    cardParams.draws = botValue(1)
    cardParams.actions = botValue(2)
    return cardParams
cardFns['Village'] = create_Village

def create_Vassal(willHitAction=None):
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(3)
    cardParams.money = botValue(2, lambda: None)
    if willHitAction is not None:
        cardParams.actions = botValue(0, lambda: None, 'Worth 1 if it hits an action card')
        cardParams.draws = botValue(0, lambda: None, 'Worth 1 if it hits an action card')
    elif willHitAction:
        cardParams.actions = botValue(1)
        cardParams.draws = botValue(1)
    elif not willHitAction:
        cardParams.actions = botValue(0)
        cardParams.draws = botValue(0)
    return cardParams
cardFns['Vassal'] = create_Vassal

def create_Bureaucrat():
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.isAttack = botValue(True)
    cardParams.cost = botValue(4)
    cardParams.doesGain = botValue(True)
    return cardParams
cardFns['Bureaucrat'] = create_Bureaucrat

def create_Militia():
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.isAttack = botValue(True)
    cardParams.cost = botValue(4)
    cardParams.money = botValue(2)
    return cardParams
cardFns['Militia'] = create_Militia

def create_Gardens(deckSize=None):
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.isVictory = botValue(True)
    cardParams.cost = botValue(4)
    if deckSize is None:
        cardParams.vp = botValue(0, lambda: None, 'Varies with deck size', 100) # This should probably always be calculated. It's safe
    elif deckSize is not None:
        cardParams.vp = botValue(math.floor(deckSize / 10))
    return cardParams
cardFns['Gardens'] = create_Gardens

def create_Smithy():
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(4)
    cardParams.draws = botValue(3)
    return cardParams
cardFns['Smithy'] = create_Smithy

def create_Moneylender(doesTrashCopper=None):
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(4)

    if doesTrashCopper is not None:
        cardParams.money = botValue(0, lambda: None, 'Worth 3 if you trash a copper')
    elif doesTrashCopper:
        cardParams.money = botValue(3)
    elif not doesTrashCopper:
        cardParams.money = botValue(0)

    cardParams.doesTrash = botValue(True)
    cardParams.beneficial = botValue(False, lambda: None)
    return cardParams
cardFns['Moneylender'] = create_Moneylender
# I think the 'does' fields should never be calculated. It should not worry about beneficiality.
# Users can figure that out for themselves.

def create_Remodel():
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(4)
    cardParams.doesGain = botValue(True)
    cardParams.doesTrash = botValue(True)
    cardParams.beneficial = botValue(False, lambda: None)
    return cardParams
cardFns['Remodel'] = create_Remodel

def create_Throne_Room(cardNameToCopy=None):
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(4)

    if cardNameToCopy is None:
        cardParams.actions = botValue(0, lambda: None, 'Worth 1 if you use it on an action (sort of)')
    elif cardNameToCopy:
        cardParams = cardFns[cardNameToCopy]()
        cardParams.isAction = botValue(True)
        cardParams.actions.value += 1

    return cardParams
cardFns['Throne Room'] = create_Throne_Room

def create_Poacher(numEmptyPiles=None):
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(4)
    cardParams.draws = botValue(1)
    cardParams.actions = botValue(1)
    cardParams.money = botValue(1)

    if numEmptyPiles is None:
        cardParams.discards = botValue(0, lambda: None, 'Discards if there are empty supply piles')
    elif numEmptyPiles is not None:
        cardParams.discards = botValue(numEmptyPiles)

    return cardParams
cardFns['Poacher'] = create_Poacher

def create_Laboratory():
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(5)
    cardParams.draws = botValue(2)
    cardParams.actions = botValue(1)
    return cardParams
cardFns['Laboratory'] = create_Laboratory

def create_Festival():
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(5)
    cardParams.actions = botValue(2)
    cardParams.money = botValue(2)
    cardParams.buys = botValue(1)
    return cardParams
cardFns['Festival'] = create_Festival

def create_Market():
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(5)
    cardParams.money = botValue(1)
    cardParams.draws = botValue(1)
    cardParams.actions = botValue(1)
    cardParams.buys = botValue(1)
    return cardParams
cardFns['Market'] = create_Market

def create_Bandit():
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.isAttack = botValue(True)
    cardParams.cost = botValue(5)
    cardParams.doesGain = botValue(True)
    return cardParams
cardFns['Bandit'] = create_Bandit

def create_Mine(hasUpgradableTreasure=None):
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(5)
    cardParams.doesTrash = botValue(True)

    if hasUpgradableTreasure is None:
        cardParams.money = botValue(1, lambda: None, 'Only worth 1 if you have an upgradable treasure', 100)
    elif hasUpgradableTreasure:
        cardParams.money = botValue(1)
    elif not hasUpgradableTreasure:
        cardParams.money = botValue(0)

    return cardParams
cardFns['Mine'] = create_Mine

def create_Council_Room():
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(5)
    cardParams.draws = botValue(4)
    cardParams.buys = botValue(1)
    return cardParams
cardFns['Council Room'] = create_Council_Room
# Incomplete - Opponent Gain

def create_Sentry():
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(5)
    cardParams.draws = botValue(1)
    cardParams.actions = botValue(1)
    cardParams.doesTrash = botValue(True)
    return cardParams
cardFns['Sentry'] = create_Sentry
# Incomplete - discarding/ordering

def create_Library(numDraws=None):
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(5)
    if numDraws is None:
        cardParams.draws = botValue(3, lambda: None, 'Draws up to 7')
    elif numDraws is not None:
        cardParams.draws = botValue(numDraws)
    return cardParams
cardFns['Library'] = create_Library
# Incomplete - discarding(sifting)?

def create_Witch():
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.isAttack = botValue(True)
    cardParams.cost = botValue(5)
    cardParams.draws = botValue(2)
    return cardParams
cardFns['Witch'] = create_Witch

def create_Artisan():
    cardParams = CardParams()
    cardParams.isAction = botValue(True)
    cardParams.cost = botValue(6)
    cardParams.doesGain = botValue(True)
    cardParams.discard = botValue(1) # Is this truly a discard? Thinkin bout Secret Passage
    return cardParams
cardFns['Artisan'] = create_Artisan

def getCard(name, paramsList=[]):
    if name not in cardFns:
        logError('name \'%s\' not found' % name)
    return Card(name, cardFns[name](*paramsList)) # funky syntax, throwing in all params (even 0)

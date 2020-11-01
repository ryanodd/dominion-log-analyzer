import math

from utils.log import logError
from alchemist.alchemistTypes import CardValue

# Used as just a parameter for constructing actual Cards.
# This makes it easy to implement every card in the game (more defaults, less writing)
# The Card fields not included in CardParams are generated from the given params.
class CardParams:
    def __init__(self):
        self.isAction = CardValue(False)
        self.isTreasure = CardValue(False)
        self.isVictory = CardValue(False)
        self.isCurse = CardValue(False)
        self.isAttack = CardValue(False)
        self.isReaction = CardValue(False)
        self.isDuration = CardValue(False)
        self.isReserve = CardValue(False)
        self.isNight = CardValue(False)

        self.cost = CardValue(0)
        self.potionCost = CardValue(0) # or bool maybe?
        self.debtCost = CardValue(0)

        self.money = CardValue(0)
        self.draws = CardValue(0)
        self.actions = CardValue(0)
        self.buys = CardValue(0)
        self.vp = CardValue(0)

        self.discards = CardValue(0)
        self.cardCostReduction = CardValue(0)

        self.doesGain = CardValue(False)
        self.doesTrash = CardValue(False)
        self.doesSift = CardValue(False)

        self.beneficial = CardValue(True)

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
        self.cardCostReduction = cardParams.cardCostReduction

        self.doesGain = cardParams.doesGain
        self.doesTrash = cardParams.doesTrash
        self.doesSift = cardParams.doesSift # First let's define what sifting is

        # Deprecated? Base only
        # Interesting one. Used for bot logic only
        self.beneficial = cardParams.beneficial

        # "Computed" values.
        # Careful with these.
        # TODO Can we have card-for-card overriding?
        self.cantrip = CardValue((self.draws.value > 0 and self.actions.value > 0 ), self.draws.messages + self.actions.messages)
        self.extraDraws = CardValue(max(0, self.draws.value - 1), self.draws.messages)
        self.extraActions = CardValue(max(0, self.actions.value - 1), self.actions.messages)
        self.terminal = CardValue(self.isAction.value and self.actions.value == 0, self.actions.messages)
        self.stops = CardValue(self.draws.value == 0, self.draws.messages)
        self.effectiveStops = CardValue(self.stops.value - self.extraDraws.value, self.extraDraws.messages + self.stops.messages)
        self.effectiveMoneyDensity = CardValue(self.money.value / max(1, self.effectiveStops.value), self.money.messages + self.effectiveStops.messages)

# Maps card names to Card constructors
cardFns = {}

# Default Values for subjective Cards should be worst-case scenario?
# We need them even when calculationNeeded for non-recursive mode

#-------------Base--------------------

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

#-----------------Dominion---------------

def create_Cellar(numDiscards=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(2)
    if numDiscards is None:
        cardParams.discards = CardValue(0, ['Dependent on number of discards'])
        cardParams.draws = CardValue(0, ['Dependent on number of discards'])
    elif numDiscards is not None:
        cardParams.discards = CardValue(numDiscards)
        cardParams.draws = CardValue(numDiscards)
    return cardParams
cardFns['Cellar'] = create_Cellar

def create_Moat():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.isReaction = CardValue(True)
    cardParams.cost = CardValue(2)
    cardParams.draws = CardValue(2)
    return cardParams
cardFns['Moat'] = create_Moat
# Incomplete - defense

def create_Chapel():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(2)
    cardParams.doesTrash = CardValue(True)
    cardParams.beneficial = CardValue(False, lambda: None) # funy
    return cardParams
cardFns['Chapel'] = create_Chapel

def create_Harbinger():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(3)
    cardParams.draws = CardValue(1)
    cardParams.actions = CardValue(1)
    return cardParams
cardFns['Harbinger'] = create_Harbinger
# Incomplete - put on top

def create_Merchant(playsSilver=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(3)
    cardParams.draws = CardValue(1)
    cardParams.actions = CardValue(1)

    if playsSilver is None:
        cardParams.money = CardValue(0, ['1 if a silver is played'])
    elif playsSilver:
        cardParams.money = CardValue(1)
    elif not playsSilver:
        cardParams.money = CardValue(0)

    return cardParams
cardFns['Merchant'] = create_Merchant

def create_Workshop():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(3)
    cardParams.doesGain = CardValue(True)
    return cardParams
cardFns['Workshop'] = create_Workshop

def create_Village():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(3)
    cardParams.draws = CardValue(1)
    cardParams.actions = CardValue(2)
    return cardParams
cardFns['Village'] = create_Village

def create_Vassal(willHitAction=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(3)
    cardParams.money = CardValue(2, lambda: None)
    if willHitAction is not None:
        cardParams.actions = CardValue(0, ['1 if it hits an action card'])
        cardParams.draws = CardValue(0, ['1 if it hits an action card'])
    elif willHitAction:
        cardParams.actions = CardValue(1)
        cardParams.draws = CardValue(1)
    elif not willHitAction:
        cardParams.actions = CardValue(0)
        cardParams.draws = CardValue(0)
    return cardParams
cardFns['Vassal'] = create_Vassal

def create_Bureaucrat():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.isAttack = CardValue(True)
    cardParams.cost = CardValue(4)
    cardParams.doesGain = CardValue(True)
    return cardParams
cardFns['Bureaucrat'] = create_Bureaucrat

def create_Militia():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.isAttack = CardValue(True)
    cardParams.cost = CardValue(4)
    cardParams.money = CardValue(2)
    return cardParams
cardFns['Militia'] = create_Militia

def create_Gardens(deckSize=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.isVictory = CardValue(True)
    cardParams.cost = CardValue(4)
    if deckSize is None:
        cardParams.vp = CardValue(0, ['Varies with deck size']) # This should probably always be calculated. It's safe
    elif deckSize is not None:
        cardParams.vp = CardValue(math.floor(deckSize / 10))
    return cardParams
cardFns['Gardens'] = create_Gardens

def create_Smithy():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(4)
    cardParams.draws = CardValue(3)
    return cardParams
cardFns['Smithy'] = create_Smithy

def create_Moneylender(doesTrashCopper=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(4)

    if doesTrashCopper is not None:
        cardParams.money = CardValue(0, ['3 if you trash a copper'])
    elif doesTrashCopper:
        cardParams.money = CardValue(3)
    elif not doesTrashCopper:
        cardParams.money = CardValue(0)

    cardParams.doesTrash = CardValue(True)
    cardParams.beneficial = CardValue(False, lambda: None)
    return cardParams
cardFns['Moneylender'] = create_Moneylender
# I think the 'does' fields should never be calculated. It should not worry about beneficiality.
# Users can figure that out for themselves.

def create_Remodel():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(4)
    cardParams.doesGain = CardValue(True)
    cardParams.doesTrash = CardValue(True)
    cardParams.beneficial = CardValue(False, lambda: None)
    return cardParams
cardFns['Remodel'] = create_Remodel

def create_Throne_Room(cardNameToCopy=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(4)

    if cardNameToCopy is None:
        cardParams.actions = CardValue(0, ['1 if you use it on an action (sort of)'])
    elif cardNameToCopy:
        cardParams = cardFns[cardNameToCopy]()
        cardParams.isAction = CardValue(True)
        cardParams.actions.value += 1

    return cardParams
cardFns['Throne Room'] = create_Throne_Room

def create_Poacher(numEmptyPiles=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(4)
    cardParams.draws = CardValue(1)
    cardParams.actions = CardValue(1)
    cardParams.money = CardValue(1)

    if numEmptyPiles is None:
        cardParams.discards = CardValue(0, ['1+ if there are empty supply piles'])
    elif numEmptyPiles is not None:
        cardParams.discards = CardValue(numEmptyPiles)

    return cardParams
cardFns['Poacher'] = create_Poacher

def create_Laboratory():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(5)
    cardParams.draws = CardValue(2)
    cardParams.actions = CardValue(1)
    return cardParams
cardFns['Laboratory'] = create_Laboratory

def create_Festival():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(5)
    cardParams.actions = CardValue(2)
    cardParams.money = CardValue(2)
    cardParams.buys = CardValue(1)
    return cardParams
cardFns['Festival'] = create_Festival

def create_Market():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(5)
    cardParams.money = CardValue(1)
    cardParams.draws = CardValue(1)
    cardParams.actions = CardValue(1)
    cardParams.buys = CardValue(1)
    return cardParams
cardFns['Market'] = create_Market

def create_Bandit():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.isAttack = CardValue(True)
    cardParams.cost = CardValue(5)
    cardParams.doesGain = CardValue(True)
    return cardParams
cardFns['Bandit'] = create_Bandit

def create_Mine(hasUpgradableTreasure=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(5)
    cardParams.doesTrash = CardValue(True)

    if hasUpgradableTreasure is None:
        cardParams.money = CardValue(1, ['0 if you don\'t have an upgradable treasure'])
    elif hasUpgradableTreasure:
        cardParams.money = CardValue(1)
    elif not hasUpgradableTreasure:
        cardParams.money = CardValue(0)

    return cardParams
cardFns['Mine'] = create_Mine

def create_Council_Room():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(5)
    cardParams.draws = CardValue(4)
    cardParams.buys = CardValue(1)
    return cardParams
cardFns['Council Room'] = create_Council_Room
# Incomplete - Opponent Gain

def create_Sentry():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(5)
    cardParams.draws = CardValue(1)
    cardParams.actions = CardValue(1)
    cardParams.doesTrash = CardValue(True)
    return cardParams
cardFns['Sentry'] = create_Sentry
# Incomplete - discarding/ordering

def create_Library(numDraws=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(5)
    if numDraws is None:
        cardParams.draws = CardValue(3, ['Dependent on hand size'])
    elif numDraws is not None:
        cardParams.draws = CardValue(numDraws)
    return cardParams
cardFns['Library'] = create_Library
# Incomplete - discarding(sifting)?

def create_Witch():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.isAttack = CardValue(True)
    cardParams.cost = CardValue(5)
    cardParams.draws = CardValue(2)
    return cardParams
cardFns['Witch'] = create_Witch

def create_Artisan():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(6)
    cardParams.doesGain = CardValue(True)
    cardParams.discard = CardValue(1) # Is this truly a discard? Topdeck? But, Thinkin bout Secret Passage
    return cardParams
cardFns['Artisan'] = create_Artisan

#-----------------Intrigue---------------

def create_Courtyard():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(2)
    cardParams.draw = CardValue(3)
    cardParams.discard = CardValue(1) # Is this truly a discard? Topdeck? But, Thinkin bout Secret Passage
    return cardParams
cardFns['Courtyard'] = create_Courtyard

def create_Lurker():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(2)
    cardParams.action = CardValue(2)
    cardParams.doesGain = CardValue(True)
    return cardParams
cardFns['Lurker'] = create_Lurker
# NOTE Not accounting for trashing from supply. doesPileControl?

def create_Pawn(choseCard=None, choseAction=None, choseBuy=None, choseMoney=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(2)

    if choseCard is None and choseAction is None and choseBuy is None and choseMoney is None:
        cardParams.draws = CardValue(1, ['Dependent on player choice'])
        cardParams.actions = CardValue(1, ['Dependent on player choice'])
        cardParams.buys = CardValue(0, ['Dependent on player choice'])
        cardParams.money = CardValue(0, ['Dependent on player choice'])
    if choseCard == True:
        cardParams.draws = CardValue(1)
    if choseAction == True:
        cardParams.actions = CardValue(1)
    if choseBuy == True:
        cardParams.buys = CardValue(1)
    if choseMoney == True:
        cardParams.money = CardValue(1)

    return cardParams
cardFns['Pawn'] = create_Pawn

def create_Masquerade():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(3)
    cardParams.doesTrash = CardValue(True)
    return cardParams
cardFns['Masquerade'] = create_Masquerade
# NOTE Not accounting for Gain (a bad card)

def create_Shanty_Town(hasNoActionCards=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(3)
    cardParams.actions = CardValue(2)
    
    if hasNoActionCards is None:
        cardParams.draws = CardValue(0, ['2 if no action cards in hand'])
    elif hasNoActionCards == True:
        cardParams.draws = CardValue(2)

    return cardParams
cardFns['Shanty Town'] = create_Shanty_Town

def create_Steward(choiceIndex=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(3)
    cardParams.doesTrash = CardValue(True)
    
    if choiceIndex is None:
        cardParams.draws = CardValue(2, ['Dependent on player choice'])
        cardParams.money = CardValue(0, ['Dependent on player choice'])
    elif choiceIndex == 0:
        cardParams.draws = CardValue(2)
    elif choiceIndex == 1:
        cardParams.money = CardValue(2)

    return cardParams
cardFns['Steward'] = create_Steward

def create_Swindler():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.isAttack = CardValue(True)
    cardParams.cost = CardValue(3)
    cardParams.money = CardValue(2)
    return cardParams
cardFns['Swindler'] = create_Swindler

def create_Wishing_Well(guessesCorrectly=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(3)
    cardParams.actions = CardValue(1)

    if guessesCorrectly is None:
        cardParams.draws = CardValue(1, ['2 if player guesses correctly'])
    elif guessesCorrectly == True:
        cardParams.draws = CardValue(2)
    elif guessesCorrectly == False:
        cardParams.draws = CardValue(1)

    return cardParams
cardFns['Wishing Well'] = create_Wishing_Well

def create_Baron(willDiscardEstate=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(4)
    cardParams.buys = CardValue(1)

    if willDiscardEstate is None:
        cardParams.money = CardValue(0, ['4 if estate is discarded'])
        cardParams.discard = CardValue(0, ['1 if estate is discarded'])
    elif willDiscardEstate == True:
        cardParams.money = CardValue(4)
        cardParams.discards = CardValue(1)
    elif willDiscardEstate == False:
        cardParams.money = CardValue(4)
    return cardParams
cardFns['Baron'] = create_Baron
# NOTE missing gaining the estate (bad)

def create_Bridge():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(4)
    cardParams.buys = CardValue(1)
    cardParams.money = CardValue(1)
    cardParams.cardCostReduction = CardValue(1)
    return cardParams
cardFns['Bridge'] = create_Bridge
# NOTE this is optimistic that cardCostReduction will be a thing and not just a simple money

def create_Conspirator(playedThreeActions=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(4)
    cardParams.money = CardValue(2)

    if playedThreeActions is None:
        cardParams.draws = CardValue(0, ['1 if player has played three actions'])
        cardParams.actions = CardValue(0, ['1 if player has played three actions'])
    elif playedThreeActions == True:
        cardParams.draws = CardValue(1)
        cardParams.actions = CardValue(1)

    return cardParams
cardFns['Conspirator'] = create_Conspirator

def create_Diplomat(hasFiveOrLessCardsInHand=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.isReaction = CardValue(True)
    cardParams.cost = CardValue(4)
    cardParams.draws = CardValue(2)

    if hasFiveOrLessCardsInHand is None:
        cardParams.actions = CardValue(0, ['2 if player has five or fewer cards in hand'])
    elif hasFiveOrLessCardsInHand == True:
        cardParams.actions = CardValue(2)

    return cardParams
cardFns['Diplomat'] = create_Diplomat
# Incomplete - defense

def create_Ironworks(gainedAction=None, gainedTreasure=None, gainedVictory=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(4)
    cardParams.doesGain = CardValue(2)

    if gainedAction is None and gainedTreasure is None and gainedVictory is None:
        cardParams.action = CardValue(0, ['1 if action card gained'])
        cardParams.money = CardValue(0, ['1 if treasure card gained'])
        cardParams.draws = CardValue(0, ['1 if victory card gained'])
    if gainedAction == True:
        cardParams.action = CardValue(1)
    if gainedTreasure == True:
        cardParams.money = CardValue(1)
    if gainedVictory == True:
        cardParams.draws = CardValue(1)

    return cardParams
cardFns['Ironworks'] = create_Ironworks

def create_Mill(willDiscardTwo=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.isVictory = CardValue(True)
    cardParams.cost = CardValue(4)
    cardParams.draws = CardValue(1)
    cardParams.actions = CardValue(1)
    cardParams.vp = CardValue(1)

    if willDiscardTwo is None:
        cardParams.money = CardValue(0, ['2 if player dicards two cards'])
    elif willDiscardTwo == True:
        cardParams.money = CardValue(2)

    return cardParams
cardFns['Mill'] = create_Mill

def create_Mining_Village(willTrash=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(4)
    cardParams.draws = CardValue(1)
    cardParams.actions = CardValue(2)

    if willTrash is None:
        cardParams.money = CardValue(0, ['2 if player trashes Mining Vilage'])
    elif willTrash == True:
        cardParams.money = CardValue(2)

    return cardParams
cardFns['Mining Village'] = create_Mining_Village

def create_Secret_Passage():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(4)
    cardParams.draws = CardValue(2)
    cardParams.actions = CardValue(1)
    return cardParams
cardFns['Secret Passage'] = create_Secret_Passage

def create_Courtier(choseAction=None, choseBuy=None, choseMoney=None, choseGold=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(5)

    if choseAction is None and choseBuy is None and choseMoney is None and choseGold is None:
        cardParams.actions = CardValue(1, ['Dependent on revealed card'])
        cardParams.buys = CardValue(1, ['Dependent on revealed card'])
        cardParams.money = CardValue(0, ['Dependent on revealed card'])
        cardParams.doesGain = CardValue(False, ['Dependent on revealed card'])
    if choseAction == True:
        cardParams.actions = CardValue(1)
    if choseBuy == True:
        cardParams.buys = CardValue(1)
    if choseBuy == True:
        cardParams.money = CardValue(3)
    if choseGold == True:
        cardParams.doesGain = CardValue(True)

    return cardParams
cardFns['Courtier'] = create_Courtier

def create_Duke(numDuchies=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.isVictory = CardValue(True)
    cardParams.cost = CardValue(5)
    if numDuchies is None:
        cardParams.vp = CardValue(0, ['Dependent on number of Duchies in deck'])
    elif numDuchies is not None:
        cardParams.vp = CardValue(numDuchies)
    return cardParams
cardFns['Duke'] = create_Duke

def create_Minion(willDiscard=None, numDiscarded=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.isAttack = CardValue(True)
    cardParams.cost = CardValue(5)
    if willDiscard is None:
        cardParams.money = CardValue(0, ['Dependent on player choice'])
        cardParams.draws = CardValue(0, ['Dependent on player choice'])
        cardParams.discards = CardValue(0, ['Dependent on player choice'])
    if willDiscard == False:
        cardParams.money = CardValue(2)
    if willDiscard == True:
        cardParams.draws = CardValue(4)
        if numDiscarded is None:
            cardParams.discards = CardValue(4, ['Dependent on hand size'])
        if willDiscard is not None:
            cardParams.discards = CardValue(numDiscarded)
    return cardParams
cardFns['Minion'] = create_Minion
# NOTE this is a 2-phase set of parameters

def create_Patrol(numExtraToDraw=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(5)
    cardParams.doesSift = CardValue(True)

    if numExtraToDraw is None:
        cardParams.draws = CardValue(3, ['Dependent on cards in deck'])
    if numExtraToDraw is not None:
        cardParams.draws = CardValue(numExtraToDraw)
    return cardParams
cardFns['Patrol'] = create_Patrol

def create_Replace():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.isAttack = CardValue(True)
    cardParams.cost = CardValue(5)
    cardParams.doesTrash = CardValue(True)
    cardParams.doesGain = CardValue(True)
    return cardParams
cardFns['Replace'] = create_Replace
# TODO topdeck?

def create_Torturer():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.isAttack = CardValue(True)
    cardParams.cost = CardValue(5)
    cardParams.draws = CardValue(3)
    return cardParams
cardFns['Torturer'] = create_Torturer

def create_Trading_Post():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(5)
    cardParams.doesTrash = CardValue(True)
    cardParams.doesGain = CardValue(True)
    return cardParams
cardFns['Trading Post'] = create_Trading_Post

def create_Upgrade():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(5)
    cardParams.draws = CardValue(1)
    cardParams.actions = CardValue(1)
    cardParams.doesTrash = CardValue(True)
    cardParams.doesGain = CardValue(True)
    return cardParams
cardFns['Upgrade'] = create_Upgrade

def create_Harem():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(6)
    cardParams.money = CardValue(2)
    cardParams.vp = CardValue(2)
    return cardParams
cardFns['Harem'] = create_Harem


def create_Nobles(choiceIndex=None):
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(6)
    cardParams.vp = CardValue(2)
    if choiceIndex is None:
        cardParams.draws = CardValue(3, ['Dependent on player choice'])
        cardParams.actions = CardValue(0, ['Dependent on player choice'])
    elif choiceIndex == 0:
        cardParams.draws = CardValue(3)
    elif choiceIndex == 1:
        cardParams.actions = CardValue(2)
    return cardParams
cardFns['Nobles'] = create_Nobles

def getCard(name, paramsList=[]):
    if name not in cardFns:
        logError('name \'%s\' not found' % name)
    return Card(name, cardFns[name](*paramsList)) # funky syntax, throwing in all params (even 0)

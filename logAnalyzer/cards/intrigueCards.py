
# -----------------Intrigue---------------

from logAnalyzer.utils.logger import logError
from logAnalyzer.logAnalyzerTypes import CardValue
from logAnalyzer.card import Card, CardParams

# Maps card names to Card constructors
cardFns = {}


def create_Courtyard():
    cardParams = CardParams()
    cardParams.isAction = CardValue(True)
    cardParams.cost = CardValue(2)
    cardParams.draw = CardValue(3)
    # Is this truly a discard? Topdeck? But, Thinkin bout Secret Passage
    cardParams.discard = CardValue(1)
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
    cardParams.draws = CardValue(2)
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
        cardParams.draws = CardValue(
            0, ['1 if player has played three actions'])
        cardParams.actions = CardValue(
            0, ['1 if player has played three actions'])
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
        cardParams.actions = CardValue(
            0, ['2 if player has five or fewer cards in hand'])
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
        cardParams.vp = CardValue(
            0, ['Dependent on number of Duchies in deck'])
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


def getIntrigueCardFns():
    return cardFns

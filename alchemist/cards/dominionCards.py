
#-----------------Dominion---------------

from utils.log import logError 
from alchemist.alchemistTypes import CardValue
from alchemist.card import Card, CardParams

# Maps card names to Card constructors
cardFns = {}

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

def getDominionCardFns():
  return cardFns

from alchemist.cards.dominionCards import getDominionCardFns
from alchemist.cards.intrigueCards import getIntrigueCardFns
from alchemist.cards.baseCards import getBaseCardFns
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
        self.stop = CardValue(self.draws.value == 0, self.draws.messages)

# Maps card names to Card constructors
cardFns = {}

cardFns.update(getBaseCardFns())
cardFns.update(getDominionCardFns())
cardFns.update(getIntrigueCardFns())

# Default Values for subjective Cards should be worst-case scenario?
# We need them even when calculationNeeded for non-recursive mode

def getCard(name, paramsList=[]):
    if name not in cardFns:
        logError('name \'%s\' not found' % name)
    return Card(name, cardFns[name](*paramsList)) # funky syntax, throwing in all params (even 0)

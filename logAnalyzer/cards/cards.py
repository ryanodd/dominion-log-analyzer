from logAnalyzer.card import Card
from logAnalyzer.cards.baseCards import getBaseCardFns
from logAnalyzer.cards.dominionCards import getDominionCardFns
from logAnalyzer.cards.intrigueCards import getIntrigueCardFns
from logAnalyzer.cards.seasideCards import getSeasideCardFns
from logAnalyzer.cards.alchemyCards import getAlchemyCardFns
from logAnalyzer.cards.prosperityCards import getProsperityCardFns
from logAnalyzer.cards.cornucopiaCards import getCornucopiaCardFns
from logAnalyzer.cards.hinterlandsCards import getHinterlandsCardFns
from logAnalyzer.cards.darkAgesCards import getDarkAgesCardFns
from logAnalyzer.cards.guildsCards import getGuildsCardFns
from logAnalyzer.cards.adventuresCards import getAdventuresCardFns
from logAnalyzer.cards.empiresCards import getEmpiresCardFns
from logAnalyzer.cards.nocturneCards import getNocturneCardFns
from logAnalyzer.cards.renaissanceCards import getRenaissanceCardFns
from logAnalyzer.cards.menagerieCards import getMenagerieCardFns
from logAnalyzer.cards.promoCards import getPromoCardFns

from logAnalyzer.utils.logger import logError

# Maps card names to Card constructors
cardFns = {}

cardFns.update(getBaseCardFns())
cardFns.update(getDominionCardFns())
cardFns.update(getIntrigueCardFns())
cardFns.update(getSeasideCardFns())
cardFns.update(getAlchemyCardFns())
cardFns.update(getProsperityCardFns())
cardFns.update(getCornucopiaCardFns())
cardFns.update(getHinterlandsCardFns())
cardFns.update(getDarkAgesCardFns())
cardFns.update(getGuildsCardFns())
cardFns.update(getAdventuresCardFns())
cardFns.update(getEmpiresCardFns())
cardFns.update(getNocturneCardFns())
cardFns.update(getRenaissanceCardFns())
cardFns.update(getMenagerieCardFns())
cardFns.update(getPromoCardFns())

# Default Values for subjective Cards should be worst-case scenario?
# We need them even when calculationNeeded for non-recursive mode


def getCard(name, paramsList=[]):
    if name not in cardFns:
        logError('name \'%s\' not found' % name)
    # funky syntax, throwing in all params (even 0)
    return Card(name, cardFns[name](*paramsList))


# -----------------Guilds---------------

from logAnalyzer.utils.logger import logError
from logAnalyzer.logAnalyzerTypes import CardValue
from logAnalyzer.card import CardParams

# Maps card names to Card constructors
cardFns = {}


def create_Candlestick_Maker():
    cardParams = CardParams()
    return cardParams


cardFns['Candlestick Maker'] = create_Candlestick_Maker


def create_Stonemason():
    cardParams = CardParams()
    return cardParams


cardFns['Stonemason'] = create_Stonemason


def create_Doctor():
    cardParams = CardParams()
    return cardParams


cardFns['Doctor'] = create_Doctor


def create_Masterpiece():
    cardParams = CardParams()
    return cardParams


cardFns['Masterpiece'] = create_Masterpiece


def create_Advisor():
    cardParams = CardParams()
    return cardParams


cardFns['Advisor'] = create_Advisor


def create_Plaza():
    cardParams = CardParams()
    return cardParams


cardFns['Plaza'] = create_Plaza


def create_Taxman():
    cardParams = CardParams()
    return cardParams


cardFns['Taxman'] = create_Taxman


def create_Herald():
    cardParams = CardParams()
    return cardParams


cardFns['Herald'] = create_Herald


def create_Baker():
    cardParams = CardParams()
    return cardParams


cardFns['Baker'] = create_Baker


def create_Butcher():
    cardParams = CardParams()
    return cardParams


cardFns['Butcher'] = create_Butcher


def create_Journeyman():
    cardParams = CardParams()
    return cardParams


cardFns['Journeyman'] = create_Journeyman


def create_Merchant_Guild():
    cardParams = CardParams()
    return cardParams


cardFns['Merchant Guild'] = create_Merchant_Guild


def create_Soothsayer():
    cardParams = CardParams()
    return cardParams


cardFns['Soothsayer'] = create_Soothsayer


def getGuildsCardFns():
    return cardFns

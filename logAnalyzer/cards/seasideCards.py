
# -----------------Seaside---------------

from logAnalyzer.utils.logger import logError
from logAnalyzer.logAnalyzerTypes import CardValue
from logAnalyzer.card import CardParams

# Maps card names to Card constructors
cardFns = {}


def create_Embargo():
    cardParams = CardParams()
    return cardParams


cardFns['Embargo'] = create_Embargo


def create_Haven():
    cardParams = CardParams()
    return cardParams


cardFns['Haven'] = create_Haven


def create_Lighthouse():
    cardParams = CardParams()
    return cardParams


cardFns['Lighthouse'] = create_Lighthouse


def create_Native_Village():
    cardParams = CardParams()
    return cardParams


cardFns['Native Village'] = create_Native_Village


def create_Pearl_Diver():
    cardParams = CardParams()
    return cardParams


cardFns['Pearl Diver'] = create_Pearl_Diver


def create_Ambassador():
    cardParams = CardParams()
    return cardParams


cardFns['Ambassador'] = create_Ambassador


def create_Fishing_Village():
    cardParams = CardParams()
    return cardParams


cardFns['Fishing Village'] = create_Fishing_Village


def create_Lookout():
    cardParams = CardParams()
    return cardParams


cardFns['Lookout'] = create_Lookout


def create_Smugglers():
    cardParams = CardParams()
    return cardParams


cardFns['Smugglers'] = create_Smugglers


def create_Warehouse():
    cardParams = CardParams()
    return cardParams


cardFns['Warehouse'] = create_Warehouse


def create_Caravan():
    cardParams = CardParams()
    return cardParams


cardFns['Caravan'] = create_Caravan


def create_Cutpurse():
    cardParams = CardParams()
    return cardParams


cardFns['Cutpurse'] = create_Cutpurse


def create_Island():
    cardParams = CardParams()
    return cardParams


cardFns['Island'] = create_Island


def create_Navigator():
    cardParams = CardParams()
    return cardParams


cardFns['Navigator'] = create_Navigator


def create_Pirate_Ship():
    cardParams = CardParams()
    return cardParams


cardFns['Pirate Ship'] = create_Pirate_Ship


def create_Salvager():
    cardParams = CardParams()
    return cardParams


cardFns['Salvager'] = create_Salvager


def create_Sea_Hag():
    cardParams = CardParams()
    return cardParams


cardFns['Sea Hag'] = create_Sea_Hag


def create_Treasure_Map():
    cardParams = CardParams()
    return cardParams


cardFns['Treasure Map'] = create_Treasure_Map


def create_Bazaar():
    cardParams = CardParams()
    return cardParams


cardFns['Bazaar'] = create_Bazaar


def create_Explorer():
    cardParams = CardParams()
    return cardParams


cardFns['Explorer'] = create_Explorer


def create_Ghost_Ship():
    cardParams = CardParams()
    return cardParams


cardFns['Ghost Ship'] = create_Ghost_Ship


def create_Merchant_Ship():
    cardParams = CardParams()
    return cardParams


cardFns['Merchant Ship'] = create_Merchant_Ship


def create_Outpost():
    cardParams = CardParams()
    return cardParams


cardFns['Outpost'] = create_Outpost


def create_Tactician():
    cardParams = CardParams()
    return cardParams


cardFns['Tactician'] = create_Tactician


def create_Treasury():
    cardParams = CardParams()
    return cardParams


cardFns['Treasury'] = create_Treasury


def create_Wharf():
    cardParams = CardParams()
    return cardParams


cardFns['Wharf'] = create_Wharf


def getSeasideCardFns():
    return cardFns

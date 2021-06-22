
# -----------------Prosperity---------------

from logAnalyzer.utils.logger import logError
from logAnalyzer.logAnalyzerTypes import CardValue
from logAnalyzer.card import CardParams

# Maps card names to Card constructors
cardFns = {}


def create_Loan():
    cardParams = CardParams()
    return cardParams


cardFns['Loan'] = create_Loan


def create_Trade_Route():
    cardParams = CardParams()
    return cardParams


cardFns['Trade Route'] = create_Trade_Route


def create_Watchtower():
    cardParams = CardParams()
    return cardParams


cardFns['Watchtower'] = create_Watchtower


def create_Bishop():
    cardParams = CardParams()
    return cardParams


cardFns['Bishop'] = create_Bishop


def create_Monument():
    cardParams = CardParams()
    return cardParams


cardFns['Monument'] = create_Monument


def create_Quarry():
    cardParams = CardParams()
    return cardParams


cardFns['Quarry'] = create_Quarry


def create_Talisman():
    cardParams = CardParams()
    return cardParams


cardFns['Talisman'] = create_Talisman


def create_Workers_Village():
    cardParams = CardParams()
    return cardParams


cardFns['Worker\'s Village'] = create_Workers_Village


def create_City():
    cardParams = CardParams()
    return cardParams


cardFns['City'] = create_City


def create_Contraband():
    cardParams = CardParams()
    return cardParams


cardFns['Contraband'] = create_Contraband


def create_Counting_House():
    cardParams = CardParams()
    return cardParams


cardFns['Counting House'] = create_Counting_House


def create_Mint():
    cardParams = CardParams()
    return cardParams


cardFns['Mint'] = create_Mint


def create_Mountebank():
    cardParams = CardParams()
    return cardParams


cardFns['Mountebank'] = create_Mountebank


def create_Rabble():
    cardParams = CardParams()
    return cardParams


cardFns['Rabble'] = create_Rabble


def create_Royal_Seal():
    cardParams = CardParams()
    return cardParams


cardFns['Royal Seal'] = create_Royal_Seal


def create_Vault():
    cardParams = CardParams()
    return cardParams


cardFns['Vault'] = create_Vault


def create_Venture():
    cardParams = CardParams()
    return cardParams


cardFns['Venture'] = create_Venture


def create_Goons():
    cardParams = CardParams()
    return cardParams


cardFns['Goons'] = create_Goons


def create_Hoard():
    cardParams = CardParams()
    return cardParams


cardFns['Hoard'] = create_Hoard


def create_Grand_Market():
    cardParams = CardParams()
    return cardParams


cardFns['Grand Market'] = create_Grand_Market


def create_Bank():
    cardParams = CardParams()
    return cardParams


cardFns['Bank'] = create_Bank


def create_Expand():
    cardParams = CardParams()
    return cardParams


cardFns['Expand'] = create_Expand


def create_Forge():
    cardParams = CardParams()
    return cardParams


cardFns['Forge'] = create_Forge


def create_Kings_Court():
    cardParams = CardParams()
    return cardParams


cardFns['King\'s Court'] = create_Kings_Court


def create_Peddler():
    cardParams = CardParams()
    return cardParams


cardFns['Peddler'] = create_Peddler


def create_Platinum():
    cardParams = CardParams()
    return cardParams


cardFns['Platinum'] = create_Platinum


def create_Colony():
    cardParams = CardParams()
    return cardParams


cardFns['Colony'] = create_Colony


def getProsperityCardFns():
    return cardFns

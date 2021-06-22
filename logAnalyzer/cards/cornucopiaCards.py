
#-----------------Cornucopia---------------

from utils.log import logError 
from logAnalyzer.logAnalyzerTypes import CardValue
from logAnalyzer.card import CardParams

# Maps card names to Card constructors
cardFns = {}

def create_Hamlet():
  cardParams = CardParams()
  return cardParams
cardFns['Hamlet'] = create_Hamlet

def create_Fortune_Teller():
  cardParams = CardParams()
  return cardParams
cardFns['Fortune Teller'] = create_Fortune_Teller

def create_Menagerie():
  cardParams = CardParams()
  return cardParams
cardFns['Menagerie'] = create_Menagerie

def create_Farming_Village():
  cardParams = CardParams()
  return cardParams
cardFns['Farming Village'] = create_Farming_Village

def create_Horse_Traders():
  cardParams = CardParams()
  return cardParams
cardFns['Horse Traders'] = create_Horse_Traders

def create_Remake():
  cardParams = CardParams()
  return cardParams
cardFns['Remake'] = create_Remake

def create_Tournament():
  cardParams = CardParams()
  return cardParams
cardFns['Tournament'] = create_Tournament

def create_Bag_of_Gold():
  cardParams = CardParams()
  return cardParams
cardFns['Bag of Gold'] = create_Bag_of_Gold

def create_Diadem():
  cardParams = CardParams()
  return cardParams
cardFns['Diadem'] = create_Diadem

def create_Followers():
  cardParams = CardParams()
  return cardParams
cardFns['Followers'] = create_Followers

def create_Princess():
  cardParams = CardParams()
  return cardParams
cardFns['Princess'] = create_Princess

def create_Trusty_Steed():
  cardParams = CardParams()
  return cardParams
cardFns['Trusty Steed'] = create_Trusty_Steed

def create_Young_Witch():
  cardParams = CardParams()
  return cardParams
cardFns['Young Witch'] = create_Young_Witch

def create_Harvest():
  cardParams = CardParams()
  return cardParams
cardFns['Harvest'] = create_Harvest

def create_Horn_of_Plenty():
  cardParams = CardParams()
  return cardParams
cardFns['Horn of Plenty'] = create_Horn_of_Plenty

def create_Hunting_Party():
  cardParams = CardParams()
  return cardParams
cardFns['Hunting Party'] = create_Hunting_Party

def create_Jester():
  cardParams = CardParams()
  return cardParams
cardFns['Jester'] = create_Jester

def create_Fairgrounds():
  cardParams = CardParams()
  return cardParams
cardFns['Fairgrounds'] = create_Fairgrounds

def getCornucopiaCardFns():
  return cardFns

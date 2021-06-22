
#-----------------Hinterlands---------------

from utils.log import logError 
from logAnalyzer.logAnalyzerTypes import CardValue
from logAnalyzer.card import CardParams

# Maps card names to Card constructors
cardFns = {}

def create_Crossroads():
  cardParams = CardParams()
  return cardParams
cardFns['Crossroads'] = create_Crossroads

def create_Duchess():
  cardParams = CardParams()
  return cardParams
cardFns['Duchess'] = create_Duchess

def create_Fools_Gold():
  cardParams = CardParams()
  return cardParams
cardFns['Fool\'s Gold'] = create_Fools_Gold

def create_Develop():
  cardParams = CardParams()
  return cardParams
cardFns['Develop'] = create_Develop

def create_Oasis():
  cardParams = CardParams()
  return cardParams
cardFns['Oasis'] = create_Oasis

def create_Oracle():
  cardParams = CardParams()
  return cardParams
cardFns['Oracle'] = create_Oracle

def create_Scheme():
  cardParams = CardParams()
  return cardParams
cardFns['Scheme'] = create_Scheme

def create_Tunnel():
  cardParams = CardParams()
  return cardParams
cardFns['Tunnel'] = create_Tunnel

def create_Jack_of_All_Trades():
  cardParams = CardParams()
  return cardParams
cardFns['Jack of All Trades'] = create_Jack_of_All_Trades

def create_Noble_Brigand():
  cardParams = CardParams()
  return cardParams
cardFns['Noble Brigand'] = create_Noble_Brigand

def create_Nomad_Camp():
  cardParams = CardParams()
  return cardParams
cardFns['Nomad Camp'] = create_Nomad_Camp

def create_Silk_Road():
  cardParams = CardParams()
  return cardParams
cardFns['Silk Road'] = create_Silk_Road

def create_Spice_Merchant():
  cardParams = CardParams()
  return cardParams
cardFns['Spice Merchant'] = create_Spice_Merchant

def create_Trader():
  cardParams = CardParams()
  return cardParams
cardFns['Trader'] = create_Trader

def create_Cache():
  cardParams = CardParams()
  return cardParams
cardFns['Cache'] = create_Cache

def create_Cartographer():
  cardParams = CardParams()
  return cardParams
cardFns['Cartographer'] = create_Cartographer

def create_Embassy():
  cardParams = CardParams()
  return cardParams
cardFns['Embassy'] = create_Embassy

def create_Haggler():
  cardParams = CardParams()
  return cardParams
cardFns['Haggler'] = create_Haggler

def create_Highway():
  cardParams = CardParams()
  return cardParams
cardFns['Highway'] = create_Highway

def create_Ill_Gotten_Gains():
  cardParams = CardParams()
  return cardParams
cardFns['Ill-Gotten Gains'] = create_Ill_Gotten_Gains

def create_Inn():
  cardParams = CardParams()
  return cardParams
cardFns['Inn'] = create_Inn

def create_Mandarin():
  cardParams = CardParams()
  return cardParams
cardFns['Mandarin'] = create_Mandarin

def create_Margrave():
  cardParams = CardParams()
  return cardParams
cardFns['Margrave'] = create_Margrave

def create_Stables():
  cardParams = CardParams()
  return cardParams
cardFns['Stables'] = create_Stables

def create_Border_Village():
  cardParams = CardParams()
  return cardParams
cardFns['Border Village'] = create_Border_Village

def create_Farmland():
  cardParams = CardParams()
  return cardParams
cardFns['Farmland'] = create_Farmland

def getHinterlandsCardFns():
  return cardFns

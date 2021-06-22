
#-----------------Promo---------------

from utils.log import logError 
from logAnalyzer.logAnalyzerTypes import CardValue
from logAnalyzer.card import CardParams

# Maps card names to Card constructors
cardFns = {}

def create_Black_Market():
  cardParams = CardParams()
  return cardParams
cardFns['Black Market'] = create_Black_Market

def create_Church():
  cardParams = CardParams()
  return cardParams
cardFns['Church'] = create_Church

def create_Dismantle():
  cardParams = CardParams()
  return cardParams
cardFns['Dismantle'] = create_Dismantle

def create_Envoy():
  cardParams = CardParams()
  return cardParams
cardFns['Envoy'] = create_Envoy

def create_Sauna():
  cardParams = CardParams()
  return cardParams
cardFns['Sauna'] = create_Sauna

def create_Avanto():
  cardParams = CardParams()
  return cardParams
cardFns['Avanto'] = create_Avanto

def create_Walled_Village():
  cardParams = CardParams()
  return cardParams
cardFns['Walled Village'] = create_Walled_Village

def create_Governor():
  cardParams = CardParams()
  return cardParams
cardFns['Governor'] = create_Governor

def create_Stash():
  cardParams = CardParams()
  return cardParams
cardFns['Stash'] = create_Stash

def create_Captain():
  cardParams = CardParams()
  return cardParams
cardFns['Captain'] = create_Captain

def create_Prince():
  cardParams = CardParams()
  return cardParams
cardFns['Prince'] = create_Prince

def getPromoCardFns():
  return cardFns

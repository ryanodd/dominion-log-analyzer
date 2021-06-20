
#-----------------Alchemy---------------

from utils.log import logError 
from alchemist.alchemistTypes import CardValue
from alchemist.card import CardParams

# Maps card names to Card constructors
cardFns = {}

def create_Transmute():
  cardParams = CardParams()
  return cardParams
cardFns['Transmute'] = create_Transmute

def create_Vineyard():
  cardParams = CardParams()
  return cardParams
cardFns['Vineyard'] = create_Vineyard

def create_Herbalist():
  cardParams = CardParams()
  return cardParams
cardFns['Herbalist'] = create_Herbalist

def create_Apothecary():
  cardParams = CardParams()
  return cardParams
cardFns['Apothecary'] = create_Apothecary

def create_Scrying_Pool():
  cardParams = CardParams()
  return cardParams
cardFns['Scrying Pool'] = create_Scrying_Pool

def create_University():
  cardParams = CardParams()
  return cardParams
cardFns['University'] = create_University

def create_Alchemist():
  cardParams = CardParams()
  return cardParams
cardFns['Alchemist'] = create_Alchemist

def create_Familiar():
  cardParams = CardParams()
  return cardParams
cardFns['Familiar'] = create_Familiar

def create_Philosophers_Stone():
  cardParams = CardParams()
  return cardParams
cardFns['Philosopher\'s Stone'] = create_Philosophers_Stone

def create_Potion():
  cardParams = CardParams()
  return cardParams
cardFns['Potion'] = create_Potion

def create_Golem():
  cardParams = CardParams()
  return cardParams
cardFns['Golem'] = create_Golem

def create_Apprentice():
  cardParams = CardParams()
  return cardParams
cardFns['Apprentice'] = create_Apprentice

def create_Possession():
  cardParams = CardParams()
  return cardParams
cardFns['Possession'] = create_Possession

def getAlchemyCardFns():
  return cardFns

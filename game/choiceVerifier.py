from game.card.card import CardType
from game.choiceID import ChoiceID

verifiers = {}

def verify_action(game, response):
    return CardType.ACTION in game.currentPlayer.hand[response].types
verifiers[ChoiceID.ACTION] = verify_action

def verify_treasure(game, response):
    return CardType.TREASURE in game.currentPlayer.hand[response].types
verifiers[ChoiceID.TREASURE] = verify_treasure

def verify_buy(game, response):
    return game.currentPlayer.action in game.currentPlayer.hand[response].types
verifiers[ChoiceID.BUY] = verify_buy

#------------



#------------

def getVerifier(choiceID):
  if choiceID in verifiers:
    return verifiers[choiceID]
  else:
    return None
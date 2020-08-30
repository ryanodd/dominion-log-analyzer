from game.card.card import CardType
from game.choiceID import ChoiceID

# For picks where there is only one valid option.

forces = {}


def force_action(game, response):
    return CardType.ACTION in game.currentPlayer.hand[response].types
forces[ChoiceID.ACTION] = force_action

def force_treasure(game, response):
    return CardType.TREASURE in game.currentPlayer.hand[response].types
forces[ChoiceID.TREASURE] = force_treasure

def force_buy(game, response):
    return game.currentPlayer.action in game.currentPlayer.hand[response].types
forces[ChoiceID.BUY] = force_buy

#------------



#------------

def getForce(choiceID):
    if choiceID in forces:
        return forces[choiceID]
    else:
        return None
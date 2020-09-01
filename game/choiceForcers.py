from game.card.card import CardType
from game.choiceID import ChoiceID

# For picks where there is only one valid option.

forcers = {}


def forcer_action(game, response):
    return CardType.ACTION in game.currentPlayer.hand[response].types
forcers[ChoiceID.ACTION] = forcer_action

def forcer_treasure(game, response):
    return CardType.TREASURE in game.currentPlayer.hand[response].types
forcers[ChoiceID.TREASURE] = forcer_treasure

def forcer_buy(game, response):
    return game.currentPlayer.action in game.currentPlayer.hand[response].types
forcers[ChoiceID.BUY] = forcer_buy

#------------



#------------

def getChoiceForcer(choiceID):
    if choiceID in forcers:
        return forcers[choiceID]
    else:
        return None
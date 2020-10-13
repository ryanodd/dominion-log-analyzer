from game.card.card import CardType
from game.choiceID import ChoiceID

# For picks where there is only one valid option.

forcers = {}

# TODO: these 3 should check for: no valid options

def forcer_action(game, playerID):
    return None
forcers[ChoiceID.ACTION] = forcer_action

def forcer_treasure(game, playerID):
    return None
forcers[ChoiceID.TREASURE] = forcer_treasure

def forcer_buy(game, playerID):
    return None
forcers[ChoiceID.BUY] = forcer_buy

#------------



#------------

def getChoiceForcer(choiceID):
    if choiceID in forcers:
        return forcers[choiceID]
    else:
        return None
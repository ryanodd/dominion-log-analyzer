from card.card import CardType

def chooseAction(player, game):
    # Always plays first available action
    actionPriorities = {}
    for i in range(len(player.hand)):
        if (CardType.ACTION in player.hand[i].types):
            actionPriorities[i] = actionPriority(player.hand[i].name)
    return max(actionPriorities, key=actionPriorities.get)

def actionPriority(name):
    if (name == "Chapel"):
        return 1 # Lowest. Should be conditional
    elif (name == "Festival"):
        return 20 # always safe
    elif (name == "Laboratory"):
        return 20 # always safe
    elif (name == "Market"):
        return 20 # always safe
    elif (name == "Smithy"):
        return 10 # safe with actions
    elif (name == "Village"):
        return 20 # always safe
    else:
        return 1

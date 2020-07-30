from game.card import CardType

def chooseAction(player, game):
    # Always plays first available action
    actionPriorities = {}
    for i in range(len(player.hand)):
        if (CardType.ACTION in player.hand[i].types):
            actionPriorities[i] = actionPriority(player.hand[i].name)
    return max(actionPriorities, key=actionPriorities.get)

def actionPriority(name):
    if (name == "Chapel"):
        return 1
    elif (name == "Festival"):
        return 15
    elif (name == "Laboratory"):
        return 20
    elif (name == "Market"):
        return 20
    elif (name == "Smithy"):
        return 10
    elif (name == "Village"):
        return 20
    else:
        return 1

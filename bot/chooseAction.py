from card.card import CardType
from bot.botCardInfo import getCardInfo

def chooseAction(player, game):
    actionPriorities = {}
    for i in range(len(player.hand)):
        if (CardType.ACTION in player.hand[i].types):
            actionPriorities[i] = actionPriority(player.hand[i].name)

    if (not actionPriorities):
        return -1 # None to choose.
    bestChoice = max(actionPriorities, key=actionPriorities.get)
    if (bestChoice == 0):
        return -1
    else: bestChoice  

def actionPriority(name):
    cardInfo = getCardInfo(name)
    if not cardInfo.beneficial:
        return 0
    elif cardInfo.actions >= 1:
        return 2
    else:
        return 1 # TODO: should somehow tiebreak terminals when it matters
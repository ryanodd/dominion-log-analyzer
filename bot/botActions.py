from utils.cardUtils import trimFromDeck
from utils.log import logBot, logError

botActions = {}

# shit
def chooseChapel(player, board, bot):
        indexesTrashing = []
        indexesCopper = []
        namesTrashing = []
        for i in range(len(player.hand)):
            if (player.hand[i].name == "Estate" or player.hand[i].name == "Curse"):
                indexesTrashing.append(i)
                namesTrashing.append(player.hand[i].name)
            elif (player.hand[i].name == "Copper"):
                if (len(indexesCopper) < 3):
                    # (Up to 3 coppers): Don't trash yet, consider keeping
                    indexesCopper.append(i)
                else:
                    indexesTrashing.append(i)
                    namesTrashing.append("Copper")
        # If adding a silver is more valuable than removing 3 coppers, keep 3 coppers
        # TODO: generalize to arbitrary number of coppers by going over all buy options (not just silver)
        if (len(indexesCopper) >= 3):
            newDeckWithCoppers = trimFromDeck(player.totalDeck(), namesTrashing)
            newDeckWithCoppers.append(board.shop[5].card) # Sliver
            atmWithCoppers = bot.calcATM(newDeckWithCoppers)
            newDeckWithoutCoppers = trimFromDeck(newDeckWithCoppers, ["Copper", "Copper", "Copper"])
            newDeckWithoutCoppers.remove(board.shop[5].card) # Silver
            atmWithoutCoppers = bot.calcATM(newDeckWithoutCoppers)
            if (atmWithoutCoppers > atmWithCoppers):
                indexesTrashing.extend(indexesCopper)
                namesTrashing.extend(["Copper", "Copper", "Copper"])
        logBot("Choosing to trash: %s" % str(namesTrashing))
        return indexesTrashing
botActions["chapel"] = chooseChapel

def getBotAction(actionName):
    if (actionName not in botActions):
        logError("Could not find bot action %s" % actionName)
    return botActions[actionName]
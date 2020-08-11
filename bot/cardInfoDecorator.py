from bot.cardInfo import getCardInfo
import copy

# Wraps objectiveCardInfo
class BotCardInfoFunctionAssigner:
    def getCardInfo(self, name, deck):
        objectiveInfo = getCardInfo(name)
        for value in getObjectMembers(objectiveInfo):
            if value.needsCalculation:
                # TODO find the calculation
                # TODO execute it
                # TODO overwrite it
                value.needsCalculation = False
        return objectiveCardInfo
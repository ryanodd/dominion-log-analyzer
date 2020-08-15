from game.choice import Choice, ChoiceID

from bot.choose.chooseAction import chooseAction
from bot.choose.chooseTreasure import chooseTreasure
from bot.choose.chooseBuy import chooseBuy
from bot.choose.chooseOther import chooseOther

# self.options = options
# if ("provincePatience" not in self.options): self.options["provincePatience"] = 0
# if ("cardsPerTerminal" not in self.options): self.options["cardsPerTerminal"] = 8
# if ("chapelEnabled" not in self.options): self.options["chapelEnabled"] = False
# if ("calcATMMath" not in self.options): self.options["calcATMMath"] = False
# if ("calcATMSim" not in self.options): self.options["calcATMSim"] = False

class Bot:
    def __init__(self, botConfig):
        # TODO: load choice config here
        return

    # TODO: Nothing special about actions, treasures, buys
    def choose(self, choice, gameState, choosingPlayer):
        if (choice.id == ChoiceID.ACTION):
            return chooseAction(choice, gameState, choosingPlayer)
        elif (choice.id == ChoiceID.TREASURE):
            return chooseTreasure(choice, gameState, choosingPlayer)
        elif (choice.id == ChoiceID.BUY):
            return chooseBuy(choice, gameState, choosingPlayer)
        else:
            return chooseOther(choice, gameState, choosingPlayer)



from game.choice import Choice, ChoiceID
from choose.choosers import getChooser

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

    def choose(self, choice, gameState, choosingPlayerIndex):
        return getChooser(choice.ChoiceID)(choice, gameState, choosingPlayerIndex)



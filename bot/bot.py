from game.choices import Choice, ChoiceID

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

    def choose(self, choice):
        if (choice.id == ChoiceID.ACTION):
            return chooseAction(choice)
        elif (choice.id == ChoiceID.TREASURE):
            return chooseTreasure(choice)
        elif (choice.id == Choice.BUY):
            return chooseBuy(choice)
        else:
            return chooseOther(choiceID)(choice, self)



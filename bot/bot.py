from game.choices import Choice

from bot.chooseAction import chooseAction
from bot.chooseTreasure import chooseTreasure
from bot.chooseBuy import chooseBuy
from bot.chooseOther import chooseOther

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

    def choose(self, choice, player, game, data = []):
        if (choice == Choice.ACTION):
            return chooseAction(player, game)
        elif (choice == Choice.TREASURE):
            return chooseTreasure(player, game)
        elif (choice == Choice.BUY):
            return chooseBuy(player, game)
        else:
            return chooseOther(choice)(player, game, data, self)



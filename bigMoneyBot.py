import log
from card import *

class BigMoneyBot:
    def __init__(self):
        # uhhhhhhh. Does this need to be an object?
        pass

    def choose(self, choice, player, board):
        if (choice == 'action'):
            return self.chooseAction(player, board)
        elif (choice == 'treasure'):
            return self.chooseTreasure(player, board)
        elif (choice == 'buy'):
            return self.chooseBuy(player, board)
        else:
            logError("unrecognized choice type: %s" % choice)

    def chooseAction(self, player, board):
        # Never perform actions
        return -1

    def chooseTreasure(self, player, board):
        # Always play first available treasure. More choices come later for the rest
        for i in range(len(player.hand)):
            if (CardType.TREASURE in player.hand[i].types):
                return i
        # No treasures found
        return -1
    
    def chooseBuy(self, player, board):
        if (player.money >= 8):
            return 2 # province
        elif (player.money >= 6):
            return 6 # gold
        elif (player.money >= 3):
            return 5 # silver
        else:
            return -1

from card import *

def estate():
    def estate_vsteps(player, board):
        player.vp += 1
    return Card("Estate", 2, [CardType.VICTORY], None, estate_vsteps)

def duchy():
    def duchy_vsteps(player, board):
        player.vp += 3
    return Card("Duchy", 5, [CardType.VICTORY], None, duchy_vsteps)

def province():
    def province_vsteps(player, board):
        player.vp += 6
    return Card("Province", 8, [CardType.VICTORY], None, province_vsteps)

def copper():
    def copper_steps(player, board):
        player.money += 1
    return Card("Copper", 0, [CardType.TREASURE], copper_steps, None)

def silver():
    def silver_steps(player, board):
        player.money += 2
    return Card("Silver", 3, [CardType.TREASURE], silver_steps, None)

def gold():
    def gold_steps(player, board):
        player.money += 3
    return Card("Gold", 6, [CardType.TREASURE], gold_steps, None)

def curse():
    def curse_vsteps(player, board):
        player.vp -= 1
    return Card("Curse", 0, [CardType.CURSE], None, curse_vsteps)

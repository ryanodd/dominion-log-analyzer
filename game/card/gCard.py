from enum import Enum

class CardType(Enum):
    ACTION = 1
    TREASURE = 2
    VICTORY = 3
    ATTACK = 4
    REACTION = 5
    CURSE = 6

class CardSet(Enum):

    PROMO = 0

    BASE = 1
    INTRIGUE = 2

    SEASIDE = 3
    ALCHEMY = 4
    PROSPERITY = 5
    CORNUCOPIA = 6
    HINTERLANDS = 7
    DARKAGES = 8
    GUILDS = 9
    ADVENTURES = 10
    EMPIRES = 11
    NOCTURNE = 12
    RENAISSANCE = 13
    MENAGERIE = 14

# Game Card. ONLY data needed to execute the game. May not end up using this.
class GCard:
    def __init__(self, name, cost, types, steps, vsteps):
        self.name = name
        self.cost = cost
        self.types = types
        self.steps = steps
        self.vsteps = vsteps

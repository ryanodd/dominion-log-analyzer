from enum import Enum

class CardType(Enum):
    ACTION = 1
    TREASURE = 2
    VICTORY = 3
    ATTACK = 4
    REACTION = 5
    CURSE = 6

class CardSet(Enum):

    BASE = 1
    INTRIGUE = 2

    SEASIDE = 3
    PROSPERITY = 4
    HINTERLANDS = 5
    DARKAGES = 6
    ADVENTURES = 7
    EMPIRES = 8
    NOCTURNE = 9
    RENAISSANCE = 10
    MENAGERIE = 11

    ALCHEMY = 12
    CORNUCOPIA = 13
    GUILDS = 14

    PROMO = 15


class GCard:
    def __init__(self, name, cost, types, steps, vsteps):
        self.name = name
        self.cost = cost
        self.types = types
        self.steps = steps
        self.vsteps = vsteps

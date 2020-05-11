import copy

from card import *

DISABLED = True


class PlayerLog:
    def __init__(self):
        self.turnStarts = {} # round number -> hand
        self.actions = {} # round number -> list of action cards played
        self.buys = {} # round number -> list of cards bought
        self.turnEnds = {} # round number -> list of cards discarded (e.g. victory cards & unused actions)
    def turnStart(self, round, hand):
        self.turnStarts[round] = copy.copy(hand)
        logCards(hand, "Turn Start")
    def playAction(self, round, card):
        if (round not in self.actions):
            self.actions[round] = []
        self.actions[round].append(card)
        log("Action: %s" % card.name)
    def buy(self, round, card):
        if (round not in self.buys):
            self.buys[round] = []
        self.buys[round].append(card)
        log("Buy: %s" % card.name)
    def turnEnd(self, round, discards):
        self.turnEnds[round] = copy.copy(discards)
        logCards(discards, "Turn End")

def log(text):
    if DISABLED: return
    print(text)

def logError(text):
    if DISABLED: return
    print("ERROR: %s" % text)

def logBot(text):
    if DISABLED: return
    print("    BOT: %s" % text)

def logCards(cards, label):
    if DISABLED: return
    print("%s: " % label, end = "")
    for i in range(len(cards)):
        print(cards[i].name, end = "")
        if (i < len(cards) - 1):
            print(", ", end = "")
    print()

import copy

ENABLED = False

class TurnLog:
    def __init__(self):
        self.startingHand = []
        self.actionsPlayed = []
        self.treasuresPlayed = []
        self.boughtCards = []
        self.moneyAvailable = 0
        self.buysAvailable = 0
        self.endingHand = []

class PlayerLog:
    def __init__(self):
        self.turns = [] # TurnLogs
    def turnStart(self, hand):
        self.turns.append(TurnLog())
        self.turns[-1].startingHand = copy.copy(hand)
        logCards(hand, "Turn Start")
    def playAction(self, card):
        self.turns[-1].actionsPlayed.append(card)
        log("Action: %s" % card.name)
    def playTreasure(self, card):
        self.turns[-1].treasuresPlayed.append(card)
        #log("Treasure: %s" % card.name)
    def buyStart(self, money, buys):
        self.turns[-1].moneyAvailable = money
        self.turns[-1].buysAvailable = buys
        log("Money: %s, Buys: %s" % (money, buys))
    def buy(self, card):
        self.turns[-1].boughtCards.append(card)
        log("Buy: %s" % card.name)
    def turnEnd(self, discards):
        self.turns[-1].endingHand = copy.copy(discards) # necessary?
        self.turns[-1].cards = self.turns[-1].endingHand + self.turns[-1].actionsPlayed + self.turns[-1].treasuresPlayed
        
        logCards(discards, "Turn End")

def logNoisy(text):
    print(text)

def logError(text):
    print("ERROR: %s" % text)

def log(text):
    if not ENABLED: return
    print(text)

def logBot(text):
    if not ENABLED: return
    print("    BOT: %s" % text)

def logGame(text):
    if not ENABLED: return
    print("%s" % text)

def logCards(cards, label):
    if not ENABLED: return
    print("%s: " % label, end = "")
    for i in range(len(cards)):
        print(cards[i].name, end = "")
        if (i < len(cards) - 1):
            print(", ", end = "")
    print()

from card import *

DISABLED = True

def log(text):
    if DISABLED: return
    print(text)

def logError(text):
    if DISABLED: return
    print("ERROR: %s" % text)

def logBot(text):
    if DISABLED: return
    print("BOT: %s" % text)

def logCards(cards, label):
    if DISABLED: return
    print("%s: " % label, end = "")
    for i in range(len(cards)):
        print(cards[i].name, end = "")
        if (i < len(cards) - 1):
            print(", ", end = "")
    print()

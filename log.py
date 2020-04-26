from card import *

def log(text):
    print(text)

def logError(text):
    print("ERROR: %s" % text)

def logCards(cards, label):
    print("%s: " % label, end = "")
    for i in range(len(cards)):
        print(cards[i].name, end = "")
        if (i < len(cards) - 1):
            print(", ", end = "")
    print()

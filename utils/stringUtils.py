from enum import Enum
from game.card.gCardFactory import getCard, cardNameDict
from utils.log import logError

# DeckString Format: "12 Copper, 2 Silver, 2 Smithy"
def cardsFromDeckString(deckString):
    returnCards = []

    class State(Enum):
        NUMBER_START = 1
        NUMBER_CONTINUE = 2
        MIDDLE_SPACE = 3
        NAME = 4
        COMMA = 5
    state = State.NUMBER_START
    currentNum = ""
    currentName = ""

    # The alg assumes correct inputs but bad inputs are still all handled gracefully
    try:
        for i in range(len(deckString)):
            if (state == State.NUMBER_START):
                currentNum += deckString[i]
                state = State.NUMBER_CONTINUE
            elif (state == State.NUMBER_CONTINUE):
                if (not deckString[i].isnumeric()):
                    state = State.MIDDLE_SPACE
                else:
                    currentNum += deckString[i]
            elif (state == State.MIDDLE_SPACE):
                currentName += deckString[i]
                state = State.NAME
            elif (state == State.NAME):
                currentName += deckString[i]
                if (currentName in cardNameDict):
                    numCardsToInsert = int(currentNum)
                    returnCards += (numCardsToInsert * [getGCard(currentName)])
                    currentNum = ""
                    currentName = ""
                    state = State.COMMA
            elif (state == State.COMMA):
                state = State.NUMBER_START
    except ValueError:
        None
    if (len(currentNum) > 0 or len(currentName) > 0):
        logError("Invalid Deck String")
    else:
        return returnCards
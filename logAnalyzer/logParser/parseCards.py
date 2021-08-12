# Returns a list of card names from a string of game log cards, e.g.
# "2 Coppers, a Bridge, a Bridge Troll, an Estate, and a Jack of All Trades."
# -> ['Copper', 'Copper', 'Bridge', 'Bridge Troll', 'Estate', 'Jack of All Trades']
# An error results in None returned

# - quantities can be [a|an|{number}]
# - can have plurals, & funky plurals like 'Platina'
# - separated by commas
# - last card is followed by 'and' (no oxford comma)
# - Sirs and Dames don't have quantity words (e.g.) "buys and gains Sir Michael"
# - sometimes equals 'nothing' e.g. 'J sets nothing aside with Church.'


from logAnalyzer.logParser.logParserUtils import stripPunctuation
from logAnalyzer.logParser.strings import *  # all prefixed with s_ or r_
from logAnalyzer.logParser.cardNameFilter import getFilteredCardName
from logAnalyzer.utils.logger import logErrorAndRaise


def parseCards(input):
    words = input.split()
    listToReturn = []
    loopIndex = 0
    while loopIndex < len(words):

        # Skip 'and'
        if words[loopIndex] == s_and:
            loopIndex += 1

        # Determine quantity
        if words[loopIndex] == s_Sir or words[loopIndex] == s_Dame:
            # Sirs and Dames don't have quantity words (e.g.) "buys and gains Sir Michael"
            cardQuantity = 1
        else:
            qtyString = words[loopIndex]
            if r_number.match(qtyString):
                cardQuantity = int(qtyString)
            elif qtyString == s_a or qtyString == s_an:
                cardQuantity = 1
            else:
                logErrorAndRaise('Couldn\'t determine quantity: ' + qtyString)
            loopIndex += 1  # processed quantity

        # loop, adding words until we know we can't
        nameBeginIndex = loopIndex
        while(loopIndex < len(words)):
            # long if-statement: need to look 2 words ahead for Bridge vs. Bridge Troll
            if getFilteredCardName(stripPunctuation(" ".join(words[nameBeginIndex:loopIndex+1]))) is not None\
                    and not (loopIndex + 1 < len(words)
                             and getFilteredCardName(stripPunctuation(" ".join(words[nameBeginIndex:loopIndex+2]))) is not None):
                break
            loopIndex += 1

        cardName = getFilteredCardName(stripPunctuation(
            " ".join(words[nameBeginIndex:loopIndex+1])))
        if (cardName is None):
            return None
        listToReturn += ([cardName] * cardQuantity)
        loopIndex += 1
    return listToReturn

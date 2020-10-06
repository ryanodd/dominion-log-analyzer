import copy
from utils.mathUtils import nCr

from utils.log import logBot, logError
from game.card.card import Card, CardType
from game.choice import Choice
from utils.cardUtils import isCardTerminal, terminalCount, cardCountByName, extraActionCount, totalDraws
from bot.cardInfo import getCardInfo

def chooseBuy(choice, gameState, choosingPlayerIndex):
    player = gameState.player[choosingPlayerIndex]
    if (player.money >= 8):
        return 2 # province
    if (False):
        return chooseBuyNextTurnATM(player, gameState)
    else:
        return chooseBuyBigMoney(player, gameState)

def chooseBuyBigMoney(player, game):
    if (player.money >= 6):
        return 6 # gold
    if (player.money >= 3):
        return 5 # silver
    else:
        return -1

def chooseBuyNextTurnATM(player, game):
    potentialDeck = copy.copy(player.totalDeck())
    shopListings = game.shop.listings
    noBuyATM = calcATM(potentialDeck)
    bestIndex = -1
    bestValueIncrease = 0
    for i in range(len(game.shop.listings)):
        card = shopListings[i].card
        if (shopListings[i].cost > player.money): continue
        
        potentialDeck.append(card)
        valueIncrease = calcATM(potentialDeck) - noBuyATM
        del potentialDeck[-1]
        if (valueIncrease > bestValueIncrease):
            bestValueIncrease = valueIncrease
            bestIndex = i
    if (bestIndex != -1):
        logBot("Choosing to buy %s based on its increase of %.2f to our ATM" % (shopListings[bestIndex].card.name, bestValueIncrease))
    return bestIndex

def calcATM(deck):
    if (True):
        return calcATM_Math(deck)
    else:
        return calcATM_Sim(deck)

def calcATM_Sim(deck):
    return 0 #TODO

# Calculate ATM - Average Turn Money
# important algorithm , currently O(n)
# TODO: incorporate terminals, connect actions & draws (draws can't happen without actions)
# TODO: separate future draws by what we know is in the discard pile vs deck, changing our odds
def calcATM_Math(deck):
    deckSize = len(deck)
    handSize = 5.0 # This can be more accurate. Subtract it from deckSize for perCard calculations? "extra cards" could be a valuable concept
    totalTerminals = terminalCount(deck)
    totalNonTerminals = deckSize - totalTerminals

    totalNonTerminalDraws = 0.0
    totalNonTerminalMoney = 0.0
    totalTerminalDraws = 0.0
    totalTerminalMoney = 0.0

    for card in deck:
        if (isCardTerminal(card)):
            totalTerminalDraws +=getCardInfo(card.name).draws.value
            totalTerminalMoney += getCardInfo(card.name).money.value
        else:
            totalNonTerminalDraws += getCardInfo(card.name).draws.value
            totalNonTerminalMoney += getCardInfo(card.name).money.value

    terminalsPerCard = totalTerminals / deckSize
    drawsPerTerminal = totalTerminalDraws / totalTerminals
    nonTerminalDrawsPerCard = totalNonTerminalDraws / deckSize

    totalExtraActions = extraActionCount(deck)
    
    # cardsPerTurnBeforeTerminals is sum(n=0 to infinity, handSize * nonTerminalDrawsPerCard^n) 
    # representing your opening hand, plus the cards you draw with your opening hand,
    # plus the cards you draw with those new cards, plus the cards you draw with THOSE new cards, etc
    if (nonTerminalDrawsPerCard < 1): # converges
        cardsPerTurnBeforeTerminals = min(deckSize, (handSize/(1-nonTerminalDrawsPerCard)))
    else: # diverges
        cardsPerTurnBeforeTerminals = deckSize

    # how likely are extra terminals to be playable? This needs to be improved involving consistency
    estimatedExtraTerminalPlayProbability = min(1, (totalExtraActions / totalTerminals) * 0.75)

    hasOneTerminalProbability = 1 - (nCr(totalNonTerminals, cardsPerTurnBeforeTerminals) * nCr(totalTerminals, 0) / nCr(deckSize, cardsPerTurnBeforeTerminals))
    cardsPerTurnAfterOneTerminal = cardsPerTurnBeforeTerminals + (hasOneTerminalProbability * drawsPerTerminal)

    remainingTerminalDrawsPerCard = (totalTerminalDraws - drawsPerTerminal) / (deckSize - 1)

    effectiveRemainingTerminalDrawsPerCard = remainingTerminalDrawsPerCard * (estimatedExtraTerminalPlayProbability)
    # cardsPerTurnAfterTerminals is sum(n=0 to infinity, cardsPerTurnAfterOneTerminal * effectiveRemainingTerminalDrawsPerCard^n)
    if (effectiveRemainingTerminalDrawsPerCard < 1): # converges
        cardsPerTurnAfterTerminals = min(deckSize, (cardsPerTurnAfterOneTerminal/(1-effectiveRemainingTerminalDrawsPerCard)))
    else: # diverges
        cardsPerTurnAfterTerminals = deckSize

    nonTerminalMoneyPerCard = totalNonTerminalMoney / deckSize
    nonTerminalMoneyPerTurn = nonTerminalMoneyPerCard * cardsPerTurnAfterTerminals
    
    moneyPerTerminal = totalTerminalMoney / totalTerminals
    firstTerminalMoney = hasOneTerminalProbability * moneyPerTerminal
    
    remainingTerminalMoneyPerCard = (totalTerminalMoney - moneyPerTerminal) / (deckSize - 1)
    extraTerminalMoney = remainingTerminalMoneyPerCard * cardsPerTurnAfterTerminals

    moneyPerTurn = nonTerminalMoneyPerTurn + firstTerminalMoney + extraTerminalMoney
    logBot("calcATM: cardsPerTurn: %s, moneyPerTurn: %s" % (cardsPerTurnAfterTerminals, moneyPerTurn))
    return moneyPerTurn
    

    # t terminals: chances of a particular t being drawn in the same hand as our played t
    # we assume we played 1 t already (otherwise no cards are affected by this equation)
    # 1 guaranteed, plus (handSize - 1) attempts of being one of the (t - 1) terminals (failures) out of (deckSize - 1). Account for getting multiple

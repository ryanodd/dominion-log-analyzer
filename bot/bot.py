import copy
from utils.mathUtils import nCr

from utils.log import logBot, logError, logNoisy
from game.card import Card, CardType
from game.choices import Choice
from utils.cardUtils import trimFromDeck, isCardTerminal, terminalCount, cardCountByName, extraActionCount, totalDraws
from bot.objectiveCardInfo import getCardInfo
from bot.botActions import getBotAction

class Bot:
    def __init__(self, options):
        self.name = "Bot"

        self.options = options
        if ("provincePatience" not in self.options): self.options["provincePatience"] = 0
        if ("cardsPerTerminal" not in self.options): self.options["cardsPerTerminal"] = 8
        if ("chapelEnabled" not in self.options): self.options["chapelEnabled"] = False
        if ("calcATMMath" not in self.options): self.options["calcATMMath"] = False
        if ("calcATMSim" not in self.options): self.options["calcATMSim"] = False

        # int representing how many turns to buy gold instead of a province
        if (self.options['provincePatience'] > 0):
            # ensure no conflicts
            pass
        self.provincePatience_waited = 0

    def choose(self, choice, player, game, data = []):
        if (choice == Choice.ACTION):
            return self.chooseAction(player, game)
        elif (choice == Choice.TREASURE):
            return self.chooseTreasure(player, game)
        elif (choice == Choice.BUY):
            return self.chooseBuy(player, game)
        else:
            return getBotAction(choice)(player, game, data, self)

    def chooseAction(self, player, game):
        # Always plays first available action
        actionPriorities = {}
        for i in range(len(player.hand)):
            if (CardType.ACTION in player.hand[i].types):
                actionPriorities[i] = self.actionPriority(player.hand[i].name)
        return max(actionPriorities, key=actionPriorities.get)

    def chooseTreasure(self, player, game):
        # Always play first available treasure. More choices come later for the rest
        for i in range(len(player.hand)):
            if (CardType.TREASURE in player.hand[i].types):
                return i
        # No treasures found
        return -1
    
    def chooseBuy(self, player, game):
        if (player.money >= 8):
            # provincePatience waits to buy its first province
            if (self.provincePatience_waited < self.options['provincePatience']):
                self.provincePatience_waited += 1
                logBot("Province Patience: wait #%s" % self.provincePatience_waited)
            else:
                return 2 # province

        if (self.options["calcATMMath"] or self.options["calcATMSim"]):
            return self.chooseBuySmartly(player, game)
        else:
            return self.chooseBuyBigMoney(player, game)

    def chooseBuyBigMoney(self, player, game):
        if (player.money >= 6):
            return 6 # gold
        if (player.money >= 3):
            return 5 # silver
        else:
            return -1

    def chooseBuySmartly(self, player, game):
        potentialDeck = copy.copy(player.totalDeck())
        shopListings = game.shop.listings
        noBuyATM = self.calcATM(potentialDeck)
        bestIndex = -1
        bestValueIncrease = 0
        for i in range(len(game.shop.listings)):
            card = shopListings[i].card
            if (shopListings[i].cost > player.money): continue

            if (card.name == "Chapel" and cardCountByName(player.totalDeck(), "Chapel") == 0 and self.options["chapelEnabled"]):
                logBot("Choosing to buy chapel since we don't have one yet")
                return i

            # Don't get this terminal if we already have too many terminals
            if (isCardTerminal(card) and self.options["cardsPerTerminal"]):
                if (terminalCount(player.totalDeck()) >= (len(player.totalDeck()) // self.options["cardsPerTerminal"])): continue
            
            potentialDeck.append(card)
            valueIncrease = self.calcATM(potentialDeck) - noBuyATM
            del potentialDeck[-1]
            if (valueIncrease > bestValueIncrease):
                bestValueIncrease = valueIncrease
                bestIndex = i
        logBot("Choosing to buy %s based on its increase of %.2f to our ATM" % (shopListings[bestIndex].card.name, bestValueIncrease))
        return bestIndex

    def calcATM(self, deck):
        if (self.options["calcATMMath"]):
            return self.calcATM_Math(deck)
        elif (self.options["calcATMSim"]):
            return self.calcATM_Sim(deck)
        else:
            logError("No calcATM method set")
    
    def calcATM_Sim(self, deck):
        import turnSim
        return turnSim.simDeckTurn(deck, 10).moneyDist[1]

    # Calculate ATM - Average Turn Money
    # important algorithm , currently O(n)
    # TODO: incorporate terminals, connect actions & draws (draws can't happen without actions)
    # TODO: separate future draws by what we know is in the discard pile vs deck, changing our odds
    def calcATM_Math(self, deck):
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
                totalTerminalDraws +=getCardInfo(card.name).draws
                totalTerminalMoney += getCardInfo(card.name).money
            else:
                totalNonTerminalDraws += getCardInfo(card.name).draws
                totalNonTerminalMoney += getCardInfo(card.name).money

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
        logNoisy("calcATM: cardsPerTurn: %s, moneyPerTurn: %s" % (cardsPerTurnAfterTerminals, moneyPerTurn))
        return moneyPerTurn
        

        # t terminals: chances of a particular t being drawn in the same hand as our played t
        # we assume we played 1 t already (otherwise no cards are affected by this equation)
        # 1 guaranteed, plus (handSize - 1) attempts of being one of the (t - 1) terminals (failures) out of (deckSize - 1). Account for getting multiple
    
    def actionPriority(self, name):
        if (name == "Chapel"):
            return 1
        elif (name == "Festival"):
            return 5
        elif (name == "Laboratory"):
            return 20
        elif (name == "Market"):
            return 20
        elif (name == "Smithy"):
            return 10
        elif (name == "Village"):
            return 20
        else:
            return 1
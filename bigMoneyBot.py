import copy

from log import *
from card import *
from botUtils import trimFromDeck, isCardTerminal, terminalCount, cardCountByName
from botKnowledge import getCardInfo

class BigMoneyBot:
    def __init__(self, options):
        self.name = "BigMoneyBot"

        self.options = options
        if ("provincePatience" not in self.options): self.options["provincePatience"] = 0
        if ("cardsPerTerminal" not in self.options): self.options["cardsPerTerminal"] = 8
        if ("chapelEnabled" not in self.options): self.options["chapelEnabled"] = False

        # int representing how many turns to buy gold instead of a province
        if (self.options['provincePatience'] > 0):
            # ensure no conflicts
            pass
        self.provincePatience_waited = 0

    def choose(self, choice, player, board):
        if (choice == 'action'):
            return self.chooseAction(player, board)
        elif (choice == 'treasure'):
            return self.chooseTreasure(player, board)
        elif (choice == 'buy'):
            return self.chooseBuy(player, board)
        elif (choice == 'chapel'):
            return self.chooseChapel(player, board)
        else:
            logError("unrecognized choice type: %s" % choice)

    def chooseAction(self, player, board):
        # Always plays first available action
        actionPriorities = {}
        for i in range(len(player.hand)):
            if (CardType.ACTION in player.hand[i].types):
                actionPriorities[i] = self.actionPriority(player.hand[i].name)
        return max(actionPriorities, key=actionPriorities.get)

    def chooseTreasure(self, player, board):
        # Always play first available treasure. More choices come later for the rest
        for i in range(len(player.hand)):
            if (CardType.TREASURE in player.hand[i].types):
                return i
        # No treasures found
        return -1
    
    def chooseBuy(self, player, board):
        if (player.money >= 8):
            
            # provincePatience waits to buy its first province
            if (self.provincePatience_waited < self.options['provincePatience']):
                self.provincePatience_waited += 1
                logBot("Province Patience: wait #%s" % self.provincePatience_waited)
                return 6 # gold

            return 2 # province

        # Should be able to remove this when we fix calcATM
        if (player.money >= 6):
            return 6 # gold

        # Otherwise choose a card based on best value added to deck
        potentialDeck = copy.copy(player.totalDeck())
        bestIndex = -1
        bestValueIncrease = 0
        for i in range(len(board.shop)):
            card = board.shop[i].card
            if (card.cost > player.money): continue

            if (card.name == "Chapel" and cardCountByName(player.totalDeck(), "Chapel") == 0 and self.options["chapelEnabled"]):
                logBot("Choosing to buy chapel since we don't have one yet")
                return i

            # Don't get this terminal if we already have too many terminals
            if (isCardTerminal(card) and (terminalCount(player.totalDeck()) >= len(player.totalDeck()) // self.options["cardsPerTerminal"])): continue
            
            potentialDeck.append(card)
            valueIncrease = self.calcATM(potentialDeck) - self.calcATM(player.totalDeck())
            del potentialDeck[-1]
            if (valueIncrease > bestValueIncrease):
                bestValueIncrease = valueIncrease
                bestIndex = i
        logBot("Choosing to buy %s based on its increase of %.2f to our ATM" % (board.shop[bestIndex].card.name, bestValueIncrease))
        return bestIndex

    def chooseChapel(self, player, board):
        indexesTrashing = []
        indexesCopper = []
        namesTrashing = []
        for i in range(len(player.hand)):
            if (player.hand[i].name == "Estate" or player.hand[i].name == "Curse"):
                indexesTrashing.append(i)
                namesTrashing.append(player.hand[i].name)
            elif (player.hand[i].name == "Copper"):
                if (len(indexesCopper) < 3):
                    # (Up to 3 coppers): Don't trash yet, consider keeping
                    indexesCopper.append(i)
                else:
                    indexesTrashing.append(i)
                    namesTrashing.append("Copper")
        # If adding a silver is more valuable than removing 3 coppers, keep 3 coppers
        # TODO: generalize to arbitrary number of coppers by going over all buy options (not just silver)
        if (len(indexesCopper) >= 3):
            newDeckWithCoppers = trimFromDeck(player.totalDeck(), namesTrashing)
            newDeckWithCoppers.append(board.shop[5].card) # Sliver
            atmWithCoppers = self.calcATM(newDeckWithCoppers)
            newDeckWithoutCoppers = trimFromDeck(newDeckWithCoppers, ["Copper", "Copper", "Copper"])
            newDeckWithoutCoppers.remove(board.shop[5].card) # Silver
            atmWithoutCoppers = self.calcATM(newDeckWithoutCoppers)
            if (atmWithoutCoppers > atmWithCoppers):
                indexesTrashing.extend(indexesCopper)
                namesTrashing.extend(["Copper", "Copper", "Copper"])
        logBot("Choosing to trash: %s" % str(namesTrashing))
        return indexesTrashing


    # Calculate ATM - Average Turn Money
    # important algorithm , currently O(n)
    # TODO: account for action chaining and terminals somehow
    def calcATM(self, deck):
        deckSize = len(deck)
        totalMoney = 0.0
        drawsPerTurn = 0.0
        for card in deck:
            totalMoney += getCardInfo(card.name).money
            drawsPerTurn += getCardInfo(card.name).draws * (5.0 / deckSize) # assumes no terminal-crashes (and no draws this turn!? solution involves limits?)
        return totalMoney * ((5.0 + drawsPerTurn) / deckSize)

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
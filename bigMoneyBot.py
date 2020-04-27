import copy

from log import *
from card import *
from botUtils import isCardTerminal, terminalCount
from botKnowledge import getCardInfo

class BigMoneyBot:
    def __init__(self, name, options):
        self.name = "BM_%s" % name

        self.options = options
        if ("provincePatience" not in self.options): self.options["provincePatience"] = 0
        if ("cardsPerTerminal" not in self.options): self.options["cardsPerTerminal"] = 8

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
        else:
            logError("unrecognized choice type: %s" % choice)

    def chooseAction(self, player, board):
        # Always plays first available action
        for i in range(len(player.hand)):
            if (CardType.ACTION in player.hand[i].types):
                return i
        return -1

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

        # Otherwise choose a card based on best value added to deck
        bestIndex = -1
        bestValueIncrease = 0
        for i in range(len(board.shop)):
            card = board.shop[i].card
            if (card.cost > player.money): continue

            # Don't get this terminal if we already have too many terminals
            if (isCardTerminal(card) and (len(player.totalDeck()) / self.options["cardsPerTerminal"] <= terminalCount(player.totalDeck()))): continue
            
            valueIncrease = self.deckValueIncrease(player.totalDeck(), card)
            if (valueIncrease > bestValueIncrease):
                bestValueIncrease = valueIncrease
                bestIndex = i
        return bestIndex

    # I don't like this formula
    def deckValue(self, deck):
        deckSize = len(deck)
        totalMoney = 0.0
        totalDraws = 0.0
        for card in deck:
            totalMoney += getCardInfo(card.name).money
            totalDraws += getCardInfo(card.name).draws
        return totalMoney / max(1, (deckSize - totalDraws))

    def deckValueIncrease(self, deck, card):
        potentialDeck = copy.copy(deck)
        potentialDeck.append(card)
        return self.deckValue(potentialDeck) - self.deckValue(deck)

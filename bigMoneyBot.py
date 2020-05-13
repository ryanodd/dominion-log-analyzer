import copy

from log import logBot, logError
from card import Card, CardType
from cardUtils import trimFromDeck, isCardTerminal, terminalCount, cardCountByName
from objectiveCardInfo import getCardInfo

class Bot:
    def __init__(self, options):
        self.name = "Bot"

        self.options = options
        if ("provincePatience" not in self.options): self.options["provincePatience"] = 0
        if ("cardsPerTerminal" not in self.options): self.options["cardsPerTerminal"] = 0
        if ("chapelEnabled" not in self.options): self.options["chapelEnabled"] = False
        if ("useCalcATM" not in self.options): self.options["useCalcATM"] = True

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
            else:
                return 2 # province

        if (self.options["useCalcATM"]):
            return self.chooseBuySmartly(player, board)
        else:
            return self.chooseBuyBigMoney(player, board)

    def chooseBuyBigMoney(self, player, board):
        if (player.money >= 6):
            return 6 # gold
        if (player.money >= 3):
            return 6 # silver

    def chooseBuySmartly(self, player, board):
        potentialDeck = copy.copy(player.totalDeck())
        noBuyATM = self.calcATM(potentialDeck)
        bestIndex = -1
        bestValueIncrease = 0
        for i in range(len(board.shop)):
            card = board.shop[i].card
            if (card.cost > player.money): continue

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
    # TODO: incorporate terminals, connect actions & draws (draws can't happen without actions)
    # TODO: separate future draws by what we know is in the discard pile vs deck, changing our odds
    def calcATM(self, deck):
        deckSize = len(deck)
        actionPlayProbability = self.actionPlayProbability(deck)
        handSize = 5.0 # This can be more accurate
        totalMoney = 0.0
        drawsPerTurn = 0.0

        totalDraws = 0.0
        totalMoney = 0.0
        totalActions = 0.0

        # collect some data
        for card in deck:
            totalDraws += getCardInfo(card.name).draws
            totalMoney += getCardInfo(card.name).money
            totalActions += getCardInfo(card.name).actions
        drawsPerCard = totalDraws / deckSize
        moneyPerCard = totalMoney / deckSize
        actionsPerCard = totalActions / deckSize

        # cardsPerTurn is sum(n=0 to infinity, handSize * drawsPerCard^n) 
        # representing your opening hand, plus the cards you draw with your opening hand,
        # plus the cards you draw with those new cards, plus the cards you draw with THOSE new cards, etc
        if (drawsPerCard < 1): # converges
            cardsPerTurn = min(deckSize, (handSize/(1-drawsPerCard)))
        else: # diverges
            cardsPerTurn = deckSize

        moneyPerTurn = moneyPerCard * cardsPerTurn
        actionsPerTurn = actionsPerCard * cardsPerTurn

        logBot("calcATM: cardsPerTurn: %s, moneyPerTurn: %s, actionsPerTurn: %s" % (cardsPerTurn, moneyPerTurn, actionsPerTurn))
        return moneyPerTurn

    # The chances [0, 1] of being able to play a particular action in the deck due to terminals.
    # Having + actions (villages) in the deck should increase this value.
    # If there are 0 or 1 terminal actions in the deck, this should be 1.
    # I think this function should treat a (1 draw 2 action) card differently than a (2 action) ie. incorporate draw. BUT does this function describe the probability of being able to play the card IF DRAWN or regarless of whether drawn?
    # BUT, this function should treat a drawing terminal the same as a non-drawing terminal (since it doesn't affect actionPlayProbability).
    def actionPlayProbability(self, deck):
        deckSize = len(deck)
        handSize = 5.0 # This can be more accurate

        # t terminals: chances of a particular t being drawn in the same hand as our played t
        # we assume we played 1 t already (otherwise no cards are affected by this equation)
        # 1 guaranteed, plus (handSize - 1) attempts of being one of the (t - 1) terminals (failures) out of (deckSize - 1). Account for getting multiple

        # for now...
        return 1
    
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
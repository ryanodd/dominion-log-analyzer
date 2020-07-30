from card.card import Card, CardType
from game.choices import Choice
from utils.log import logError

cardNameDict = {}
######################### Essentials ###############################

def estate():
    def estate_vsteps(player, game):
        player.vp += 1
    return Card("Estate", 2, [CardType.VICTORY], None, estate_vsteps)
cardNameDict['Estate'] = estate


def duchy():
    def duchy_vsteps(player, game):
        player.vp += 3
    return Card("Duchy", 5, [CardType.VICTORY], None, duchy_vsteps)
cardNameDict['Duchy'] = duchy

def province():
    def province_vsteps(player, game):
        player.vp += 6
    return Card("Province", 8, [CardType.VICTORY], None, province_vsteps)
cardNameDict['Province'] = province

def copper():
    def copper_steps(player, game):
        player.money += 1
    return Card("Copper", 0, [CardType.TREASURE], copper_steps, None)
cardNameDict['Copper'] = copper

def silver():
    def silver_steps(player, game):
        player.money += 2
    return Card("Silver", 3, [CardType.TREASURE], silver_steps, None)
cardNameDict['Silver'] = silver

def gold():
    def gold_steps(player, game):
        player.money += 3
    return Card("Gold", 6, [CardType.TREASURE], gold_steps, None)
cardNameDict['Gold'] = gold

def curse():
    def curse_vsteps(player, game):
        player.vp -= 1
    return Card("Curse", 0, [CardType.CURSE], None, curse_vsteps)
cardNameDict['Curse'] = curse


######################### Base Set 2ed ############################

def artisan():
    def artisan_steps(player, game):
        # Gain card costing up to 5
        gainChoice = player.bot.choose(Choice.ARTISAN1, player, game)
        if (game.shop.listings[gainChoice].cost > 5):
            logError("Cheater! Invalid artisan gain choice")
        gainedCard = game.gain(gainChoice, player)
        player.gain(gainedCard)

        # Put a card from your hand onto your deck
        topdeckChoice = player.bot.choose(Choice.ARTISAN2, player, game)
        topdeckCard = player.hand.pop(topdeckChoice)
        player.deck.append(topdeckCard)
    return Card("Artisan", 6, [CardType.ACTION], artisan_steps, None)
cardNameDict['Artisan'] = artisan

def bandit():
    def bandit_steps(player, game):
        goldCard = game.gain(6, player)
        player.gain(goldCard)

        for opponent in game.otherPlayers(player):
            topTwoCards = []
            topTwoCards.append(opponent.deck.pop())
            topTwoCards.append(opponent.deck.pop())
            trashCandidates = []
            trashCandidatesMap = {} # maps trashCandidates indices to topTwoCards indices
            for i in range(topTwoCards):
                card = topTwoCards[i]
                if (CardType.TREASURE in card.types and card.name != "Copper"):
                    trashCandidatesMap[len(trashCandidates)] = i
                    trashCandidates.append(card)
            if (len(trashCandidates) > 0):
                trashChoice = 0
                if (len(trashCandidates) > 1):
                    trashChoice = player.bot.choose(Choice.BANDIT, opponent, game, trashCandidates)
                game.trash.append(topTwoCards[trashCandidatesMap[trashChoice]])
                trashCandidates.remove(trashChoice)
            opponent.discard += trashCandidates # discard the rest
    return Card("Bandit", 5, [CardType.ACTION], bandit_steps, None)
cardNameDict['Bandit'] = bandit
                    

def bureaucrat():
    def bureaucrat_steps(player, game):
        silverCard = game.gain(5, player)
        player.deck.append(silverCard) # not being logged as a gain for player?

        for opponent in game.otherPlayers(player):
            topDeckCandidates = []
            topDeckCandidatesMap = {} # maps topDeckCoices indices to hand indices
            for i in range(opponent.hand):
                card = opponent.hand[i]
                if CardType.VICTORY in card.types:
                    topDeckCandidatesMap[len(topDeckCandidates)] = i
                    topDeckCandidates.append(card)
            if (topDeckCandidates > 0):
                topDeckChoice = 0
                if (topDeckCandidates > 1):
                    topDeckChoice = player.bot.choose(Choice.BUREAUCRAT, opponent, game, topDeckCandidates)
                topDeckCard = opponent.hand.pop(topDeckCandidatesMap[topDeckChoice])
                opponent.deck.append(topDeckCard)
    return Card("Bureaucrat", 4, [CardType.ACTION], bureaucrat_steps, None)
cardNameDict['Bureaucrat'] = bureaucrat

def cellar():
    def cellar_steps(player, game):
        player.actions += 1
        discardChoices = player.bot.choose(Choice.CELLAR, player, game)
        numDiscarded = len(discardChoices)
        for i in sorted(discardChoices, reverse=True):
            player.discard.append(player.hand.pop(i))
        player.draw(numDiscarded)
    return Card("Cellar", 2, [CardType.ACTION], cellar_steps, None)
cardNameDict['Cellar'] = cellar

def chapel():
    def chapel_steps(player, game):
        trashChoices = player.bot.choose('chapel', player, game)
        for i in sorted(trashChoices, reverse=True):
            game.trash.append(player.hand.pop(i))

    return Card("Chapel", 2, [CardType.ACTION], chapel_steps, None)
cardNameDict['Chapel'] = chapel

def councilRoom():
    def councilRoom_steps(player, game):
        player.draw(4)
        player.buys += 1
        for opponent in game.otherPlayers(player):
            opponent.draw(1)
    return Card("Council Room", 5, [CardType.ACTION], councilRoom_steps, None)
cardNameDict['Council Room'] = councilRoom

def festival():
    def festival_steps(player, game):
        player.actions += 2
        player.buys += 1
        player.money += 2
    return Card("Festival", 5, [CardType.ACTION], festival_steps, None)
cardNameDict['Festival'] = festival

def gardens():
    def garden_vsteps(player, game):
        player.vp += len(player.totalDeck) / 10
    return Card("Gardens", 4, [CardType.VICTORY], None, garden_vsteps)
cardNameDict['Gardens'] = gardens

def harbinger():
    def harbinger_steps(player, game):
        player.draw(1)
        player.actions += 1

        topDeckChoice = player.bot.choose(Choice.HARBINGER, player, game)
        topDeckCard = player.discard.pop(topDeckChoice)
        player.deck.append(topDeckCard)
    return Card("Harbinger", 3, [CardType.ACTION], harbinger_steps, None)
cardNameDict['Harbinger'] = harbinger

def laboratory():
    def laboratory_steps(player, game):
        player.draw(2)
        player.actions += 1
    return Card("Laboratory", 5, [CardType.ACTION], laboratory_steps, None)
cardNameDict['Laboratory'] = laboratory

def library():
    def library_steps(player, game):
        cardsToDiscard = []
        while len(player.hand < 7):
            drawnCard = player.deck.pop()
            if (CardType.ACTION in drawnCard.types):
                willDiscard = player.bot.choose(Choice.LIBRARY, player, game, drawnCard)
                if (willDiscard):
                    cardsToDiscard.append(drawnCard)
                else:
                    player.hand.append(drawnCard)
        player.discard += cardsToDiscard
    return Card("Library", 5, [CardType.ACTION], library_steps, None)
cardNameDict['Library'] = library

def market():
    def market_steps(player, game):
        player.draw(1)
        player.actions += 1
        player.buys += 1
        player.money += 1
    return Card("Market", 5, [CardType.ACTION], market_steps, None)
cardNameDict['Market'] = market

# This one is trouble. Needs event triggers
# def merchant():

def militia():
    def militia_steps(player, game):
        player.money += 2

        for opponent in game.otherPlayers(player):
            while (len(opponent.hand) > 3):
                discardChoice = opponent.bot.choose(Choice.MILITIA, opponent, game)
                opponent.discard.append(opponent.hand.pop(discardChoice))
    return Card("Militia", 4, [CardType.ACTION, CardType.ATTACK], militia_steps, None)
cardNameDict['Militia'] = militia

def mine():
    def mine_steps(player, game):
        trashCandidates = []
        trashCandidatesMap = {} # maps trashCandidates indices to hand indices
        for i in range(len(player.hand)):
            card = player.hand[i]
            if (CardType.TREASURE in card.types):
                trashCandidatesMap[len(trashCandidates)] = i
                trashCandidates += card
        if (len(trashCandidates) > 0):
            trashChoice = 0
            if (len(trashCandidates) > 1):
                trashChoice = player.bot.choose(Choice.MINE1, player, game, trashCandidates)
            if (trashChoice != -1):
                trashCard = player.hand.pop(trashChoice)
                game.trash.append(trashCard)
                gainCandidates = []
                gainCandidatesMap = {} # maps gainCandidates indices to shop listing indices
                for i in range(len(game.shop.listings)):
                    listing = game.shop.listings[i]
                    if (listing.quantity > 0 and CardType.TREASURE in listing.card.types and (listing.cost - trashCard.cost) <= 3):
                        gainCandidatesMap[len(gainCandidates)] = i
                        gainCandidates += listing.card
                if (len(gainCandidates) > 0):
                    gainChoice = 0
                    if (len(gainCandidates) > 1):
                        gainChoice = player.bot.choose(Choice.MINE2, player, game, gainCandidates)
                    player.discard.append(game.gain(gainCandidatesMap[gainChoice]))
    return Card("Mine", 5, [CardType.ACTION], mine_steps, None)
cardNameDict['Mine'] = mine

# def moat():

def moneylender():
    def moneylender_steps(player, game):
        trashCandidates = []
        trashCandidatesMap = {} # maps trashCandidates indices to hand indices
        for i in range(len(player.hand)):
            card = player.hand[i]
            if (card.name == "Copper"):
                trashCandidatesMap[len(trashCandidates)] = i
                trashCandidates += card
        if (len(trashCandidates) > 0):
            trashChoice = 0
            if (len(trashCandidates) > 1):
                trashChoice = player.bot.choose(Choice.MONEYLENDER, player, game, trashCandidates)
            if (trashChoice != -1):
                trashCard = player.hand.pop(trashChoice)
                game.trash.append(trashCard)
                player.money += 3
    return Card("Moneylender", 4, [CardType.ACTION], moneylender_steps, None)
cardNameDict['Moneylender'] = moneylender

def poacher():
    def poacher_steps(player, game):
        player.draw(1)
        player.actions += 1
        player.money += 1
        numToDiscard = 0
        for listing in game.shop.listings:
            if (listing.quantity == 0):
                numToDiscard += 1
        for _ in range(numToDiscard):
            if (len(player.hand) > 0):
                discardChoice = player.bot.choose(Choice.POACHER, player, game)
                player.discard.append(player.hand.pop(discardChoice))
    return Card("Poacher", 4, [CardType.ACTION], poacher_steps, None)
cardNameDict['Poacher'] = poacher

def remodel():
    def remodel_steps(player, game):
        if (len(player.hand) > 0):
            trashChoice = player.bot.choose(Choice.REMODEL1, player, game)
            trashCard = player.hand.pop(trashChoice)
            game.trash.append(trashCard)

            gainCandidates = []
            gainCandidatesMap = {} # maps gainCandidates indices to shop listing indices
            for i in range(len(game.shop.listings)):
                listing = game.shop.listings[i]
                if (listing.quantity > 0 and (listing.cost - trashCard.cost) <= 2):
                    gainCandidatesMap[len(gainCandidates)] = i
                    gainCandidates += listing.card
            if (len(gainCandidates) > 0):
                gainChoice = 0
                if (len(gainCandidates) > 1):
                    gainChoice = player.bot.choose(Choice.REMODEL2, player, game, gainCandidates)
                player.discard.append(game.gain(gainCandidatesMap[gainChoice]))
    return Card("Remodel", 4, [CardType.ACTION], remodel_steps, None)
cardNameDict['Remodel'] = remodel

def sentry():
    def sentry_steps(player, game):
        player.draw(1)
        player.actions += 1
        sentryCards = []
        for _ in range(2):
            if (len(player.deck) == 0):
                player.reshuffle()
            if (len(player.deck) > 0):
                sentryCards.append(player.deck.pop())

        if (len(sentryCards) > 0):
            trashChoices = player.bot.choose(Choice.SENTRY1, player, game, sentryCards)
            for i in sorted(trashChoices, reverse=True):
                game.trash.append(sentryCards.pop(i))
        if (len(sentryCards) > 0):
            discardChoices = player.bot.choose(Choice.SENTRY2, player, game, sentryCards)
            for i in sorted(discardChoices, reverse=True):
                player.discard.append(sentryCards.pop(i))
        if (len(sentryCards) > 0):
            orderChoice = [0]
            if (len(sentryCards) > 1):
                orderChoice = player.bot.choose(Choice.SENTRY3, player, game, sentryCards)
            # Thinkin bout having SENTRY3 (order choice) be 1 card choice at a time?
            # To preserve index correctness, we don't pop from sentryCards (it dies after this function anyway)
            for o in orderChoice:
                player.deck.append(sentryCards[o])
    return Card("Sentry", 5, [CardType.ACTION], sentry_steps, None)
cardNameDict['Sentry'] = sentry

def smithy():
    def smithy_steps(player, game):
        player.draw(3)
    return Card("Smithy", 4, [CardType.ACTION], smithy_steps, None)
cardNameDict['Smithy'] = smithy

def throneRoom():
    def throneRoom_steps(player, game):
        playCandidates = []
        playCandidatesMap = {} # maps playCandidates indices to hand indices
        for i in range(len(player.hand)):
            card = player.hand[i]
            if (CardType.ACTION in card):
                playCandidatesMap[len(playCandidates)] = i
                playCandidates.append(card)
        if (len(playCandidates) > 0):
            playChoice = player.bot.choose(Choice.THRONEROOM, player, game, playCandidates)
            if (playChoice != -1):
                playCard = player.hand.pop(playCandidatesMap[playChoice])
                player.play.append(playCard)
                playCard.steps()
                playCard.steps()
    return Card("Throne Room", 4, [CardType.ACTION], throneRoom_steps, None)
cardNameDict['Throne Room'] = throneRoom

def vassal():
    def vassal_steps(player, game):
        player.money += 2
        if (len(player.deck) == 0):
            player.reshuffle()
        if (len(player.deck) > 0):
            discardCard = player.deck.pop()
            willPlay = player.bot.choose(Choice.VASSAL, player, game, discardCard)
            if (willPlay):
                player.play.append(discardCard)
                discardCard.steps()
            else:
                player.discard.append(discardCard)
    return Card("Vassal", 3, [CardType.ACTION], vassal_steps, None)
cardNameDict['Vassal'] = vassal

def village():
    def village_steps(player, game):
        player.draw(1)
        player.actions += 2
    return Card("Village", 3, [CardType.ACTION], village_steps, None)
cardNameDict['Village'] = village

def witch():
    def witch_steps(player, game):
        player.draw(2)
        for opponent in game.otherPlayers(player):
            if (game.shop.listings[3].quantity > 0):
                opponent.discard.append(game.gain(3))
    return Card("Witch", 5, [CardType.ACTION, CardType.ATTACK], witch_steps, None)
cardNameDict['Witch'] = witch

def workshop():
    def workshop_steps(player, game):
        gainCandidates = []
        gainCandidatesMap = {} # maps gainCandidates indices to shop listing indices
        for i in range(len(game.shop.listings)):
            listing = game.shop.listings[i]
            if (listing.quantity > 0 and listing.cost <= 4):
                gainCandidatesMap[len(gainCandidates)] = i
                gainCandidates += listing.card
        if (len(gainCandidates) > 0):
            gainChoice = 0
            if (len(gainCandidates) > 1):
                gainChoice = player.bot.choose(Choice.WORKSHOP, player, game, gainCandidates)
            player.discard.append(game.gain(gainCandidatesMap[gainChoice]))
    return Card("Workshop", 3, [CardType.ACTION, CardType.ATTACK], workshop_steps, None)
cardNameDict['Workshop'] = workshop

def getCard(name):
    if (name not in cardNameDict):
        logError("Name %s not found in cardNameDict")
    return cardNameDict[name]()
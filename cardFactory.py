from card import *

cardFactoryList = []
######################### Essentials ###############################

def estate():
    def estate_vsteps(player, board):
        player.vp += 1
    return Card("Estate", 2, [CardType.VICTORY], None, estate_vsteps)
cardFactoryList.append(estate)


def duchy():
    def duchy_vsteps(player, board):
        player.vp += 3
    return Card("Duchy", 5, [CardType.VICTORY], None, duchy_vsteps)
cardFactoryList.append(duchy)

def province():
    def province_vsteps(player, board):
        player.vp += 6
    return Card("Province", 8, [CardType.VICTORY], None, province_vsteps)
cardFactoryList.append(province)

def copper():
    def copper_steps(player, board):
        player.money += 1
    return Card("Copper", 0, [CardType.TREASURE], copper_steps, None)
cardFactoryList.append(copper)

def silver():
    def silver_steps(player, board):
        player.money += 2
    return Card("Silver", 3, [CardType.TREASURE], silver_steps, None)
cardFactoryList.append(silver)

def gold():
    def gold_steps(player, board):
        player.money += 3
    return Card("Gold", 6, [CardType.TREASURE], gold_steps, None)
cardFactoryList.append(gold)

def curse():
    def curse_vsteps(player, board):
        player.vp -= 1
    return Card("Curse", 0, [CardType.CURSE], None, curse_vsteps)
cardFactoryList.append(curse)


######################### Base Set 2ed ############################

# def artisan():

# def bandit():

# def bureaucrat():

# def cellar():

def chapel():
    def chapel_steps(player, board):
        trashChoices = player.bot.choose('chapel', player, board)
        for i in sorted(trashChoices, reverse=True):
            board.trash.append(player.hand.pop(i))

    return Card("Chapel", 2, [CardType.ACTION], chapel_steps, None)
cardFactoryList.append(chapel)

# def councilRoom():

def festival():
    def festival_steps(player, board):
        player.actions += 2
        player.buys += 1
        player.money += 2
    return Card("Festival", 5, [CardType.ACTION], festival_steps, None)
cardFactoryList.append(festival)

def gardens():
    def garden_vsteps(player, board):
        player.vp += len(player.totalDeck) / 10
    return Card("Gardens", 4, [CardType.VICTORY], None, garden_vsteps)
cardFactoryList.append(gardens)

# def harbinger():

def laboratory():
    def laboratory_steps(player, board):
        player.draw(2)
        player.actions += 1
    return Card("Laboratory", 5, [CardType.ACTION], laboratory_steps, None)
cardFactoryList.append(laboratory)

# def library():

def market():
    def market_steps(player, board):
        player.draw(1)
        player.actions += 1
        player.buys += 1
        player.money += 1
    return Card("Market", 5, [CardType.ACTION], market_steps, None)
cardFactoryList.append(market)

# def merchant():

# def militia():

# def mine():

# def moat():

# def moneylender():

# def poacher():

# def remodel():

# def sentry():

def smithy():
    def smithy_steps(player, board):
        player.draw(3)
    return Card("Smithy", 4, [CardType.ACTION], smithy_steps, None)
cardFactoryList.append(smithy)

# def throneRoom():

# def vassal():

def village():
    def village_steps(player, board):
        player.draw(1)
        player.actions += 2
    return Card("Village", 3, [CardType.ACTION], village_steps, None)
cardFactoryList.append(village)

# def witch():

# def workshop():

def getCardFactoryList():
    return cardFactoryList

def getCardNameDict():
    cardNameDict = {}
    for cardFactory in cardFactoryList:
        card = cardFactory()
        cardNameDict[card.name] = card
    return cardNameDict

cardNameDict = getCardNameDict()
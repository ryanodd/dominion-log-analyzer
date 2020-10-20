def cardCountByName(cards, name):
    count = 0
    for card in cards:
        if (card.name == name):
            count += 1
    return count

def cardCountByType(cards, type):
    count = 0
    for card in cards:
        if (type in card.types):
            count += 1
    return count
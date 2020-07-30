from card.card import CardType

def chooseTreasure(player, game):
    # Always play first available treasure. More choices come later for the rest
    for i in range(len(player.hand)):
        if (CardType.TREASURE in player.hand[i].types):
            return i
    # No treasures found
    return -1
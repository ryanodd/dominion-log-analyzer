from card.card import CardType
from bot.cardInfo import getCardInfo

def chooseTreasure(player, game):
    # Always play first available treasure. More choices come later for the rest
    for i in range(len(player.hand)):
        if (CardType.TREASURE in player.hand[i].types and getCardInfo(player.hand[i].name).beneficial):
            return i
    # No treasures found
    return -1
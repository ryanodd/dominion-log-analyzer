from game.card.gCard import CardType
from bot.cardInfo import getCardInfo

def chooseTreasure(choice, gameState, choosingPlayer):
    # Always play first available treasure. More choices come later for the rest
    for i in range(len(choosingPlayer.hand)):
        if (CardType.TREASURE in choosingPlayer.hand[i].types and getCardInfo(choosingPlayer.hand[i].name).beneficial):
            return i
    # No treasures found
    return -1
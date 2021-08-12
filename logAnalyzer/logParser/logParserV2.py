

lineFns = {}


def l_gameId(line):
    None


lineFns['Game #{number}, unrated.'] = l_gameId


def l_startsWith(line):
    None


lineFns['{A} starts with {cards}.'] = l_startsWith


def l_turn(line):
    None


lineFns['Turn {number} - {name}'] = l_turn


# Only for start of turn effects
def l_turnStart(line):
    None


lineFns['{A} starts their turn.'] = l_turnStart


def l_shuffle(line):
    None


lineFns['{A} shuffles their deck.'] = l_shuffle


#
# Draw
#

def l_draw(line):
    None


lineFns['{A} draws {cards}.'] = l_draw


def l_drawWithBrackets(line):
    None


lineFns['draws {cards} ({item}).'] = l_drawWithBrackets


def l_drawWithBracketsFrom(line):
    None


lineFns['draws {cards} (from {item}).'] = l_drawWithBracketsFrom

#
# Play
#


def l_play(line):
    None


lineFns['{A} plays {cards}.'] = l_play


def l_playMoney(line):
    None


lineFns['{A} plays {cards}. (+${number})'] = l_playMoney

#
# Gain
#


def l_buyGain(line):
    None


lineFns['{A} buys and gains {cards}.'] = l_buyGain


def l_gain(line):
    None


lineFns['{A} gains {cards}.'] = l_gain


def l_gainFromTrash(line):
    None


lineFns['{A} gains {cards} from trash.'] = l_gainFromTrash


def l_gainOntoDeck(line):
    None


lineFns['{A} gains {cards} onto their draw pile.'] = l_gainOntoDeck


#
# Trash
#


# Can be from hand or supply (Lurker)
def l_trash(line):
    None


lineFns['{A} trashes {cards}.'] = l_trash


def l_trashBrackets(line):
    None


lineFns['{A} trashes {cards} ({item}).'] = l_trashBrackets


#
# Gets
#

def l_getActions(line):
    None


lineFns['{A} gets +{number} [Action|Actions].'] = l_getActions


def l_getActionsFromBrackets(line):
    None


lineFns['{A} gets +{number} [Action|Actions] (from {item}).'] = l_getActionsFromBrackets


def l_getBuys(line):
    None


lineFns['{A} gets +{number} [Buy|Buys].'] = l_getBuys


def l_getBuysFromBrackets(line):
    None


lineFns['{A} gets +{number} [Buy|Buys] (from {item}).'] = l_getBuysFromBrackets


def l_getMoney(line):
    None


lineFns['{A} gets +${number}.'] = l_getMoney


def l_getMoneyFromBrackets(line):
    None


lineFns['{A} gets +{number} Coin (from {item}).'] = l_getMoneyFromBrackets


def l_getVP(line):
    None


lineFns['{A} gets {number}VP.'] = l_getVP


def l_getVPFrom(line):
    None


lineFns['{A} gets {number}VP from {item}.'] = l_getVPFrom


#
# Put In Hand
#

def l_putInHand(line):
    None


lineFns['{A} puts {cards} into their hand.'] = l_putInHand


def l_putInHandBrackets(line):
    None


lineFns['{A} puts {cards} in hand ({item}).'] = l_putInHandBrackets


#
# Put in Deck
#


def l_putBottomDeck(line):
    None


lineFns['{A} puts {cards} on the bottom of their deck.'] = l_putBottomDeck


def l_putBottomDrawPile(line):
    None


lineFns['{A} puts {cards} on the bottom of Draw Pile.'] = l_putBottomDrawPile


def l_putBackOnDeck(line):
    None


lineFns['{A} puts {cards} back onto their deck.'] = l_putBackOnDeck


def l_topdeck(line):
    None


lineFns['{A} topdecks {cards}.'] = l_topdeck


def l_insertIntoDeck(line):
    None


lineFns['{A} inserts {cards} into their deck.'] = l_insertIntoDeck


#
# Reveal / Look
#

def l_reveal(line):
    None


lineFns['{A} reveals {cards}.'] = l_reveal


def l_revealAndFinally(line):
    None


lineFns['{A} reveals {cards} and finally {card}.'] = l_revealAndFinally


def l_revealHand(line):
    None


lineFns['{A} reveals their hand: {cards}.'] = l_revealHand


def l_look(line):
    None


lineFns['{A} looks at {cards}.'] = l_look

#
# Set Aside
#


def l_setAside(line):
    None


lineFns['{A} sets {cards} aside.'] = l_setAside


def l_setAsideWith(line):
    None


lineFns['{A} sets {cards} aside with {item}.'] = l_setAsideWith


#
# Return
#


def l_return(line):
    None


lineFns['{A} returns {cards}.'] = l_return


def l_returnToPile(line):
    None


lineFns['{A} returns {cards} to {pile}.'] = l_returnToPile

#
# Misc
#


def l_receive(line):
    None


lineFns['{A} receives {cards}.'] = l_receive


def l_block(line):
    None


lineFns['{A} blocks with {cards}.'] = l_block


def l_endBuyPhase(line):
    None


lineFns['{A} ends their buy phase.'] = l_endBuyPhase


def l_moveDeckToDiscard(line):
    None


lineFns['{A} moves their deck to the discard.'] = l_moveDeckToDiscard


def l_name(line):
    None


lineFns['{A} names {card}.'] = l_name


def l_react(line):
    None


lineFns['{A} reacts with {cards}.'] = l_react


def l_skipDraw(line):
    None


lineFns['{A} skips a draw (because of {item}).'] = l_skipDraw

#
# Boon
#


def l_takeBoon(line):
    None


lineFns['{A} takes {boon}.'] = l_takeBoon


def l_setAsideBoon(line):
    None


lineFns['{A} sets {boon} aside.'] = l_setAsideBoon


def l_receiveBoon(line):
    None


lineFns['{A} receives {boon}.'] = l_receiveBoon


def l_discardBoon(line):
    None


lineFns['{A} discards {boon}.'] = l_discardBoon


def l_skysGiftFailDiscard(line):
    None


lineFns['{A} fails to discard for the Sky\'s Gift.'] = l_skysGiftFailDiscard


#
# Hex
#


def l_takeHex(line):
    None


lineFns['{A} takes {hex}.'] = l_takeHex


def l_setAsideHex(line):
    None


lineFns['{A} sets {hex} aside.'] = l_setAsideHex


def l_receiveHex(line):
    None


lineFns['{A} receives {hex}.'] = l_receiveHex


def l_discardHex(line):
    None


lineFns['{A} discards {hex}.'] = l_discardHex


#
# State
#


def l_takeState(line):
    None


lineFns['{A} takes {state}.'] = l_takeState


def l_returnState(line):
    None


lineFns['{A} returns {state}.'] = l_returnState


#
# Artifact
#

def l_takeArtifact(line):
    None


lineFns['{A} takes {artifact}.'] = l_takeArtifact

#
# Debt
#


def l_takeDebt(line):
    None


lineFns['{A} takes {number} debt.'] = l_takeDebt


def l_takeDebtFromPile(line):
    None


lineFns['{A} takes {number} debt from {pile}.'] = l_takeDebtFromPile


def l_repayDebt(line):
    None


lineFns['{A} repays {number} debt.'] = l_repayDebt


def l_takeDebtWithRemaining(line):
    None


lineFns['{A} repays {number} debt ({number} remaining).'] = l_takeDebtWithRemaining


#
# Landmarks
#

def l_takeVPFromLandmark(line):
    None


lineFns['{A} takes {number} VP from {landmark}.'] = l_takeVPFromLandmark


def l_moveVPToLandmark(line):
    None


lineFns['{A} moves {number}VP from {pile} to {landmark}.'] = l_moveVPToLandmark


#
# Exile
#


def l_exile(line):
    None


lineFns['{A} exiles {cards}.'] = l_exile


def l_disacardFromExile(line):
    None


lineFns['{A} discards {cards} from Exile.'] = l_disacardFromExile


#
# Tavern Mat
#


def l_putTavernMat(line):
    None


lineFns['{A} puts {cards} on their Tavern mat.'] = l_putTavernMat


def l_call(line):
    None


lineFns['{A} calls {cards}.'] = l_call

#
# Tokens
#


def l_minusCardTokenToDeck(line):
    None


lineFns['{A} moves -Card token to Draw Pile.'] = l_minusCardTokenToDeck


def l_minusCardTokenToLimbo(line):
    None


lineFns['{A} moves -Card token to Token Limbo.'] = l_minusCardTokenToLimbo


def l_trashTokenToPile(line):
    None


lineFns['{A} moves Trashing token to {pile}.'] = l_trashTokenToPile


def l_minusCostTokenToPile(line):
    None


lineFns['{A} moves -Cost token to {pile}.'] = l_minusCostTokenToPile


def l_cardTokenToPile(line):
    None


lineFns['{A} moves +Card token to {pile}.'] = l_cardTokenToPile


def l_coinTokenToPile(line):
    None


lineFns['{A} moves +Coin token to {pile}.'] = l_coinTokenToPile


def l_actionTokenToPile(line):
    None


lineFns['{A} moves +Action token to {pile}.'] = l_actionTokenToPile


def l_buyTokenToPile(line):
    None


lineFns['{A} moves +Buy token to {pile}.'] = l_buyTokenToPile


#
# Coffers
#


def l_useCoffers(line):
    None


lineFns['{A} uses {number} Coffers. (+${number}).'] = l_useCoffers


def l_getCoffers(line):
    None


lineFns['{A} gets +{number} Coffers.'] = l_getCoffers


def l_getCoffersBrackets(line):
    None


lineFns['{A} gets +{number} Coffers. ({project})'] = l_getCoffersBrackets


#
# Villagers
#

def l_useVillagers(line):
    None


lineFns['{A} uses {number} [Villager|Villagers].'] = l_useVillagers


def l_getVillagers(line):
    None


lineFns['{A} gets +{number} [Villager|Villagers].'] = l_getVillagers


def l_getVillagersBrackets(line):
    None


lineFns['{A} gets +{number} [Villager|Villagers]. ({item})'] = l_getVillagersBrackets


#
# Ways
#

def l_playUsing(line):
    None


lineFns['{A} plays {cards} using {way}.'] = l_playUsing


def l_useWay(line):
    None


lineFns['{A} uses {way}.'] = l_useWay


def l_wouldGet(line):
    None


lineFns['{A} would get +${number}.'] = l_wouldGet


#
# Card Specific
#


def l_passes(line):
    None


lineFns['{A} passes {cards} to {A}.'] = l_passes


def l_wishFail(line):
    None


lineFns['{A} wishes for {card} but reveals {card}'] = l_wishFail


def l_wishSuccess(line):
    None


lineFns['{A} wishes for {card} and finds it.'] = l_wishSuccess


def l_putIslandMat(line):
    None


lineFns['{A} puts {cards} on their Island mat.'] = l_putIslandMat


def l_getTactitian(line):
    None


lineFns['{A} gets +1 Buy, +1 Action and draws {cards} (Tactician).'] = l_getTactitian


def l_flipJourneyToken(line):
    None


lineFns['{A} flips Journey token face [up|down].'] = l_flipJourneyToken


def l_inherit(line):
    None


lineFns['{A} inherits {cards}.'] = l_inherit


def l_returnTokenBridgeTroll(line):
    None


lineFns['{A} returns -Coin token set by Bridge Troll (-$1).'] = l_returnTokenBridgeTroll


def l_druidSetAside(line):
    None


lineFns['Druid sets {boon} aside.'] = l_druidSetAside

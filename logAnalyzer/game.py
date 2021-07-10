class Player:
    def __init__(self):
        # Weird case. Sometimes we can know player initial without name.
        self.name = None
        # In those cases we use initial, so we need a default.
        self.initial = 'X'
        self.totalDeckCardNames = []
        self.deckCardNames = []
        self.handCardNames = []
        self.discardNames = []

        # I think duration cards can just stay "in play"
        self.playCardNames = []

        # Native Village mat, Island mat, Tavern mat
        self.matCardNames = []

        self.exileCardNames = []


class Game:
    def __init__(self):
        self.players = []
        #self.vpRemaining = gameInfoParams.vpRemaining

    def getPlayerByInitial(self, initial):
        for player in self.players:
            if player.initial == initial:
                return player
        return None

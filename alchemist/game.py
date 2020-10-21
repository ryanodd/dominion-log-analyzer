class Player:
    def __init__(self):
        self.name = None # Weird case. Sometimes we can know player initial without name.
        self.initial = 'X' # In those cases we use initial, so we need a default.
        self.cardNames = []

class Game:
    def __init__(self):
        self.players = []
        #self.vpRemaining = gameInfoParams.vpRemaining

    def getPlayerByInitial(self, initial):
        for player in self.players:
            if player.initial == initial:
                return player
        return None
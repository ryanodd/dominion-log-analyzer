class GameInfoParams:
    def __init__(self):
        self.vpRemaining = botValue(-1, None, 100)

    # Woah. I wonder if this is good or bad. memory & performance
    def reset(self):
        self.__init__()

# This class makes card-agnostic algorithms possible. I'm down to rename it
class GameInfo:
    def __init__(self, gameInfoParams):
        self.vpRemaining = gameInfoParams.vpRemaining
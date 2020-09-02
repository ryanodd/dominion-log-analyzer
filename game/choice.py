from enum import Enum
from game.choiceVerifiers import getChoiceVerifier
from game.choiceForcers import getChoiceForcer
from game.choiceID import ChoiceID

class ResponseType(Enum):
    INDEX = 1
    INDEXES = 2
    ENUM = 3
    BOOL = 4
    ID = 5

class Choice:
    def __init__(self, choiceID, responseType):
        self.id = choiceID
        self.responseType = responseType
        self.verifier = getChoiceVerifier(choiceID)
        self.force = getChoiceForcer(choiceID)

choices = {}

choices[ChoiceID.ACTION]        = Choice(ChoiceID.ACTION, ResponseType.INDEX)
choices[ChoiceID.TREASURE]      = Choice(ChoiceID.TREASURE, ResponseType.INDEX)
choices[ChoiceID.BUY]           = Choice(ChoiceID.BUY, ResponseType.INDEX)

choices[ChoiceID.ARTISAN1]      = Choice(ChoiceID.ARTISAN1, ResponseType.ID)
choices[ChoiceID.ARTISAN2]      = Choice(ChoiceID.ARTISAN2, ResponseType.INDEX)
choices[ChoiceID.BANDIT]        = Choice(ChoiceID.BANDIT, ResponseType.INDEX)
choices[ChoiceID.BUREAUCRAT]    = Choice(ChoiceID.BUREAUCRAT, ResponseType.INDEX)
choices[ChoiceID.CELLAR]        = Choice(ChoiceID.CELLAR, ResponseType.INDEXES)
choices[ChoiceID.CHAPEL]        = Choice(ChoiceID.CHAPEL, ResponseType.INDEXES)
choices[ChoiceID.HARBINGER]     = Choice(ChoiceID.HARBINGER, ResponseType.INDEX)
choices[ChoiceID.LIBRARY]       = Choice(ChoiceID.LIBRARY, ResponseType.BOOL)
choices[ChoiceID.MILITIA]       = Choice(ChoiceID.MILITIA, ResponseType.INDEXES)
choices[ChoiceID.MINE1]         = Choice(ChoiceID.MINE1, ResponseType.INDEX)
choices[ChoiceID.MINE2]         = Choice(ChoiceID.MINE2, ResponseType.ID)
choices[ChoiceID.MONEYLENDER]   = Choice(ChoiceID.MONEYLENDER, ResponseType.INDEX)
choices[ChoiceID.POACHER]       = Choice(ChoiceID.POACHER, ResponseType.INDEXES)
choices[ChoiceID.REMODEL1]      = Choice(ChoiceID.REMODEL1, ResponseType.INDEX)
choices[ChoiceID.REMODEL2]      = Choice(ChoiceID.REMODEL2, ResponseType.ID)
choices[ChoiceID.SENTRY1]       = Choice(ChoiceID.SENTRY1, ResponseType.INDEXES)
choices[ChoiceID.SENTRY2]       = Choice(ChoiceID.SENTRY2, ResponseType.INDEXES)
choices[ChoiceID.SENTRY3]       = Choice(ChoiceID.SENTRY3, ResponseType.INDEXES)
choices[ChoiceID.THRONEROOM]    = Choice(ChoiceID.THRONEROOM, ResponseType.INDEX)
choices[ChoiceID.VASSAL]        = Choice(ChoiceID.VASSAL, ResponseType.BOOL)
choices[ChoiceID.WORKSHOP]      = Choice(ChoiceID.WORKSHOP, ResponseType.ID)

def getChoice(choiceID):
    return choices[choiceID]
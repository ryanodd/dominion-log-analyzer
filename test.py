from saveLogToDB import saveLogToDB
from logAnalyzer.logParser.logParserUtils import getGameIdFromLog
from logAnalyzer.deckReport.deckListReport import getDeckListReport
from logAnalyzer.logParser.logParser import logToGame

file = open("logAnalyzer/logParser/samples/bruh.txt")
fileStr = file.read()
file.close()

saveLogToDB(fileStr)

game = logToGame(fileStr)

deckReports = []
for player in game.players:
    deckReports.append(getDeckListReport(player))

# expectedDecks = {}
# expectedDecks['J'] = ['']
# # assert(game.)

for deckReport in deckReports:
    print(deckReport['playerInitial'] + ' - ' + deckReport['playerName'])
    print('---')
    for card in deckReport['cardNameList']:
        print(card)
    print()

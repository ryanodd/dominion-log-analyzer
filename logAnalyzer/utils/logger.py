from saveLogToDB import saveErrorToDB
import sys


def logGame(game):
    print('GAME:')
    for player in game.players:
        print(player.name, '  (', player.initial, ')')
        for card in player.totalDeckCardNames:
            print('    ', card)


def logError(message):
    print('ERROR:')
    print(message)


def logErrorAndExit(message):
    logError(message)
    saveErrorToDB(message)
    print('EXITING...')
    sys.exit(1)

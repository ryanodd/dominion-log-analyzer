from saveLogToDB import saveErrorToDB, saveLogToDB
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


def logErrorAndRaise(message):
    logError(message)
    print('EXITING...')
    raise Exception(message)

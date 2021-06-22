import sys


def logError(message):
    print('ERROR:')
    print(message)


def logErrorAndExit(message):
    logError(message)
    print('EXITING...')
    sys.exit(1)

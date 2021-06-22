import json
from logAnalyzer.utils.logger import logGame
from logAnalyzer.logParser.logParser import logToGame
from logAnalyzer.deckReport.deckListReport import getDeckListReport


def lambda_handler(event, context):
    payload = json.loads(event['body'])
    gameLogStr = payload['logStr']
    print('GAME LOG:')
    print(gameLogStr)

    game = logToGame(gameLogStr)

    logGame(game)

    deckReports = []
    for player in game.players:
        deckReports.append(getDeckListReport(player))

    returnJson = json.dumps({
        'deckReports': deckReports
    })

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': returnJson
    }

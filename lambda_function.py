import json
import traceback
from logAnalyzer.utils.logger import logGame
from logAnalyzer.logParser.logParser import logToGame
from logAnalyzer.deckReport.deckListReport import getDeckListReport


def lambda_handler(event, context):
    try:
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
    except Exception as e:
        exc = traceback.format_exc()
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'text/plain'
            },
            'body': exc
        }

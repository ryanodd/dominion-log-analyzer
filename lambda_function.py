import json
from logAnalyzer.logParser.logParser import logToGame
from logAnalyzer.deckReport.deckReport import getDeckReport


def lambda_handler(event, context):
  payload = json.load(event.body)

  game = logToGame(payload['logStr'])

  deckReports = []
  for player in game.players:
    deckReports.append(getDeckReport(player))

  # Unused error snippet
  if False:
    return {
      'statusCode': 500
    }

  return {
    'statusCode': 200,
    'headers': {
      'Content-Type': 'application/json'
    },
    'body': {
      'deckReports': deckReports
    }
  }

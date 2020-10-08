from bottle import route, run, template, response, request
import json

from game.gameState import GameState
from utils.dominionOnlineLogParser.logParser import logToGameState

@route('/logParser', method=['POST'])
def parseThatLogBoi():
    response.headers['Bing-Bong-Test-Header'] = "aboobidydoo"
    response.headers['Content-Type'] = "application/json"
    
    payload = json.load(request.body)
    gameState = logToGameState(payload['logStr'])
    print(gameState)
    if len(gameState.players) != 2:
        response.status = 500
        return {"error": "you messed up! this log is not a 2p game"}
    deck1List = []
    for card in gameState.players[0].deck:
        deck1List.append(card.name)
    deck2List = []
    for card in gameState.players[1].deck:
        deck2List.append(card.name)

    return {"deck1List": deck1List, "deck2List": deck2List}
    
run(host='localhost', port=3993, debug=True)
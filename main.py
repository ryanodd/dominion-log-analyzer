from bottle import route, run, template, response, request
import json

from game.gameState import GameState
from utils.dominionOnlineLogParser.logParser import logToGameState

@route('/logParser', method=['POST'])
def parseThatLogBoi():
    response.headers['Bing-Bong-Test-Header'] = "aboobidydoo"
    response.headers['Content-Type'] = "application/json"
    
    payload = json.load(request.body)
    print(payload['logStr'])
    gameState = logToGameState(payload['logStr'])
    
    if gameState.players != 2:
        response.status = 500
        return {"error": "you messed up! this log is not a 2p game"}
    deck1List = gameState.players[0].deck
    deck2List = gameState.players[1].deck

    print('got here')

    returnPayload = {"deck1List": deck1List, "deck2List": deck2List}
    return {"payload": returnPayload}#template('<b>Hello dooooood</b>!')
    
run(host='localhost', port=3993, debug=True)
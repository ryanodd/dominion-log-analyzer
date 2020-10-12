from bottle import route, run, template, response, request
import json
import os

from game.gameState import GameState
from utils.dominionOnlineLogParser.logParser import logToGameState
from utils.cardSorter import sortCardsByTypeThenCost

# CORS decorator
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        if request.get_header('Origin').startswith('https'):
            response.headers['Access-Control-Allow-Origin'] = 'https://councilroom.herokuapp.com'
        else:
            response.headers['Access-Control-Allow-Origin'] = 'http://councilroom.herokuapp.com'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors

@route('/logParser', method=['POST', 'OPTIONS'])
@enable_cors
def parseThatLogBoi():
    payload = json.load(request.body)

    gameState = logToGameState(payload['logStr'])
    if False:
        response.status = 500

    #   DeckInfo:
    #   playerName: string
    #   playerInitial: string
    #   cardNameList: string[]
    #   numCards: number
    #   totalMoney: number
    #   totalStops: number
    #   totalDraw: number
    #   totalTerminals: number
    #   totalVillages: number

    deckInfos = []
    for player in gameState.players:
        deckInfo = {}
        deckInfo['playerName'] = player.name
        deckInfo['playerInitial'] = player.name[0]
        
        deckInfo['cardNameList'] = []
        player.deck = sortCardsByTypeThenCost(player.deck)
        for card in player.deck:
            deckInfo['cardNameList'].append(card.name)
        
        deckInfo['numCards'] = len(player.deck)
        deckInfo['totalMoney'] = 0
        deckInfo['totalStops'] = 0
        deckInfo['totalDraw'] = 0
        deckInfo['totalExtraDraw'] = 0
        deckInfo['totalActions'] = 0
        deckInfo['totalTerminals'] = 0
        deckInfo['totalExtraActions'] = 0
        deckInfo['totalBuys'] = 0

        deckInfos.append(deckInfo)

    response.headers['Content-Type'] = "application/json"
    return {'deckInfos': deckInfos}

if 'PORT' in os.environ.keys():
    run(host='0.0.0.0', port=os.environ['PORT'])
else:
    run(host='localhost', port=3993)

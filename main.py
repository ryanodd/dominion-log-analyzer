from bottle import route, run, template, response, request
import json

from game.gameState import GameState
from utils.dominionOnlineLogParser.logParser import logToGameState
from utils.cardSorter import sortCardsByTypeThenCost

@route('/logParser', method=['POST'])
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
    
run(host='localhost', port=3993, debug=True)


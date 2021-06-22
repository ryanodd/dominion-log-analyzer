from bottle import route, run, template, response, request
import json
import os

from logAnalyzer.logParser.logParser import logToGame
from logAnalyzer.deckReport.deckReport import getDeckReport

# CORS decorator


def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        if 'IS_PROD' in os.environ.keys():
            if request.get_header('Origin').startswith('https'):
                response.headers['Access-Control-Allow-Origin'] = 'https://councilroom.herokuapp.com'
            else:
                response.headers['Access-Control-Allow-Origin'] = 'http://councilroom.herokuapp.com'
        else:
            response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors


@route('/logParser', method=['POST', 'OPTIONS'])
@enable_cors
def parseThatLogBoi():
    response.headers['Content-Type'] = "application/json"
    payload = json.load(request.body)

    game = logToGame(payload['logStr'])

    deckReports = []
    for player in game.players:
        deckReports.append(getDeckReport(player))

    # Unused error snippet
    if False:
        response.status = 500

    return {'deckReports': deckReports}


if 'PORT' in os.environ.keys():
    run(host='0.0.0.0', port=os.environ['PORT'])
else:
    run(host='localhost', port=3993)

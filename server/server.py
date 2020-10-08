from bottle import route, run, template, response, request

@route('/logParser', method=['POST'])
def index():
    response.headers['Bing-Bong-Test-Header'] = "aboobidydoo"
    response.headers['Content-Type'] = "application/json"
    return {"data": "hhhh"}#template('<b>Hello dooooood</b>!')
    
run(host='localhost', port=3993, debug=True)
import bottle
bottle.TEMPLATE_PATH = ['template']

from bottle import Bottle, run, template

app = Bottle()

@app.route('/')
@app.route('/<name:re:[a-z]+>')
def index(name='world'):
    return template('script-01', name=name)

run(app, host='localhost', port=8080)
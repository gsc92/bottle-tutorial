from bottle import Bottle, run

app = Bottle()

@app.route('/o')
def hello():
    return "Hello guest, How Are You?"

run(app, host='localhost', port=8080)
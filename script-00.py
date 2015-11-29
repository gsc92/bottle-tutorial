from bottle import Bottle, run, redirect

app = Bottle()

@app.route('/hello')
def hello():
    redirect("/world")

@app.route('/world')
def world():
    return "World!"

run(app, host='localhost', port=8080)
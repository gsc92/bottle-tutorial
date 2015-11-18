from bottle import run,route,template

@route('/hello')
def hello():
	return "Hello World!"



run( host='localhost', port=8080)
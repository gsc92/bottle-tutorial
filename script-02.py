from bottle import error,run,app


@error(404)
def error404(error):
    return 'Nothing here, sorry'


run(app, host='localhost', port=8080)
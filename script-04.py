from bottle import request, route, template, run

@route('/hello')
def hello():
    name = request.cookies.username or 'Guest'
    return template('Hello {{name}}', name=name)

run(host='localhost', port=8081)
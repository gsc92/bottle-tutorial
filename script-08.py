from bottle import run, route, view

@route('/hello')
@route('/hello/<name>')
@view('hello_template')  #--> what does it do?
def hello(name='World'):
    return dict(name=name)


#@route('/hello')
#@route('/hello/<name>')
#def hello(name='World'):
#    return template('hello_template', name=name)

run(host='localhost', port=8080)
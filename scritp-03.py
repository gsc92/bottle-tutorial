from bottle import response, run, route

@route('/iso')
def get_iso():
    response.content_type = 'ISO-8859-15'
    return u'This will be sent with ISO-8859-15 encoding.'

@route('/latin9')
def get_latin():
    response.content_type = 'text/html; charset=latin9'
    return u'ISO-8859-15 is also known as latin9.'

run(host='localhost', port=8081)
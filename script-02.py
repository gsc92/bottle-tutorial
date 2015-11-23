from bottle import route, run, static_file


@route('/desktop/<file_name>')
def serve_desktop(file_name):
    return static_file(file_name, root='C://Users/GOKCE/Desktop/')

@route('/desktop/homepage/<file_name>')
def serve_homepage(file_name):
    return static_file(file_name, root='C://Users/GOKCE/Desktop/Homepage/')

run(host='localhost', port=8080)
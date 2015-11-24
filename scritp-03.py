from bottle import static_file, route, run

from bottle import static_file
@route('/images/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root='./static/', mimetype='image/jpg')

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')

run(host='localhost', port=8081)
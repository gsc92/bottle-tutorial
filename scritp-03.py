from bottle import static_file, route, run

from bottle import route, abort
@route('/restricted')
def restricted():
    abort(401, "Sorry, access denied.")

run(host='localhost', port=8081)
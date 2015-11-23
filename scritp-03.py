from bottle import redirect, route, run


@route('/wrong/url')
def wrong():
    redirect("/right/url")

run(host='localhost', port=8088)
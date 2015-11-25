from bottle import run, route, request, template


@route('/my_ip')
def show_ip():
    # ip = request.get('REMOTE_ADDR')
    ip = request.get('REMOTE_ADDR')
    #ip = request['REMOTE_ADDR']
    return template("Your IP is: {{ip}}", ip=ip)


run(host='localhost', port=8081)

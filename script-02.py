from bottle import request,route,run,static_file


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='C://Users/GOKCE/Desktop/1.jpg')


run(host='localhost', port=8080)
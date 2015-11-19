from bottle import static_file,route, run

from bottle import static_file
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='C:\\Users\GOKCE\Desktop\1.jpg')


run(host='localhost', port=8082)
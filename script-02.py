from bottle import static_file,route, run

@route('/static/<filename>')
def server_static(file_name):
    return static_file(file_name, root='/C:/Desktop/1.jpg')


run(host='localhost', port=8080)
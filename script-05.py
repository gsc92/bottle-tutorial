from bottle import request, run, route

@route('/upload', method='POST')

def do_upload():
    category = request.forms.get('category')
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'

    save_path = category
    upload.save(save_path)# appends upload.filename automatically
    return 'OK'

run(host='localhost', port=8081)
from bottle import request,run

r=request.get("https://github.com/", auth=('user', 'pass'))

print(r.status_code)
print(r.headers['content-type'])


run( host='localhost', port=8080)
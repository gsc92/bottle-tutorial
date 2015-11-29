from bottle import run, request

for choice in request.forms.getall('multiple_choice'):
    print(choice)

run(host='localhost', port=8080)
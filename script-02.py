from bottle import error,run,route


@route('/wiki/<pagename>')            # matches /wiki/Learning_Python
@route('<pagename:re:[A-Z]+>')

def show_wiki_page(pagename):
    print('[show-wiki-page]', pagename)
    return pagename




run( host='localhost', port=8080)
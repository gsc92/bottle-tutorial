from bottle import route, install, template, run
from bottle_sqlite import SQLitePlugin
import bottle_werkzeug

install(SQLitePlugin(dbfile='C:/Users/GOKCE/Desktop/my.db'))
install(bottle_werkzeug.Plugin())

@route('/')
def main(db):
    assert db

@route('/article/<article_id:int>')
def article(db, article_id):
    assert article_id > 0

@route('/show/<post_id:int>')
def show(db, post_id):
    c = db.execute('SELECT title, content FROM posts WHERE id = ?', (post_id,))
    row = c.fetchone()
    return template('show_post', title=row['title'], text=row['content'])

run(host="localhost", port=8080, debug=True)
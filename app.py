#bottle is the equalent to Node express 
from bottle import run, view, static_file, get
import sqlite3


##########################################
@get("/app.css")
def do():
    return static_file("app.css", root="css")

##########################################
@get("/logo.png")
def do():
    return static_file("logo.png", root="images")

#########################################
@get("/")
@view("index")
def do():
    db = sqlite3.connect("data/database.db")
    items = db.execute("SELECT * FROM items ORDER BY RANDOM() LIMIT 21").fetchall()
    db.close()
    return dict(items=items)

########################################
@get("/items/<item_id>")
@view("item")
def do(item_id):
    db = sqlite3.connect("./data/database.db")
    item = db.execute("SELECT * FROM items WHERE item_id = ?", (item_id,)).fetchone()
    print(item)
    db.close()
    return dict(item=item)

########################################
# reloader=True is the same as nodemon
# the server is called paste
run(host="localhost", port=5555, debug=True, reloader=True, server="paste")

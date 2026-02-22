from flask import Flask, render_template, redirect, url_for
from database import exist_db, create_list, DB_PATH

import sqlite3
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("startPage.html")

@app.route("/startPage", methods=["POST"])
def createList():
    exist_db()
    list_id, list_nuber = create_list()
    return redirect(url_for("showList", list_id=list_id))

@app.route("/list/<int:list_id>")
def showList(list_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    list_info = conn.execute("SELECT * FROM lists WHERE id = ?", (list_id, )).fetchone()

    list_number = conn.execute("SELECT * FROM items WHERE list_id = ?", (list_id, )).fetchall()

    conn.close()

    return  render_template("list.html", list_info=list_info, list_number=list_number)



if __name__ == "__main__":
    app.run(debug=True)


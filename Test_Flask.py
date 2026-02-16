from flask import Flask, render_template

app = Flask(__name__)


# That is a new comment.
@app.route("/")
def home():
    return render_template("index.html")


from flask import Flask

app = Flask(__name__)


@app.route("/requestClave")

def requestClave():
    return
# pyrefly: ignore [missing-import]
from flask import Flask 

app = Flask(__name__)

@app.route("/hello")
def hell_world():
    return "<h1>Hello, Denzel!</h1>"
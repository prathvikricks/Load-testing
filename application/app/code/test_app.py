from flask import Flask
from random import randint
from time import sleep

app = Flask(__name__)

@app.route("/")
def index():
    return "OK"

@app.route("/about")
def about():
    return "its about"

@app.route("/random")
def random():
    sleep(randint(0, 2))
    return "its late"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

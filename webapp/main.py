
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/researcher-app")
def researcher_app():
    name = request.args.get("name")
    message = f"Hello {name}" if name else "Hello world"
    return render_template("app.html", name=name, message=message)

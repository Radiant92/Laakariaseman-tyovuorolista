from flask import render_template
from application import app
from application.viikko.models import Viikko
@app.route("/")
def index():
    return render_template("index.html", overflow=Viikko.find_overflow())
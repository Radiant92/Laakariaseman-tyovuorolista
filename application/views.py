from flask import render_template
from application import app
from application.auth.models import User
@app.route("/")
def index():
    return render_template("index.html", needs_work=User.find_users_under_40_hours_work())
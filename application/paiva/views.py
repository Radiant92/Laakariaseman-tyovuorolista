from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.paiva.models import Paiva

@app.route("/paivat/show/<int:id>", methods=["GET"])
@login_required(role="ANY")
def paivat_show(id):
    paiva = Paiva.query.filter(Paiva.id==id).first()
    return render_template("paivat/show.html", paiva=paiva)
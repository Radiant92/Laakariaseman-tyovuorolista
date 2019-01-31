from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application import app, db
from application.kiireellisyysluokka.models import Kiireellisyysluokka
from application.kiireellisyysluokka.forms import KiireellisyysluokkaForm

@app.route("/kiireellisyysluokat", methods=["GET"])
@login_required
def kiireellisyysluokat_index():
    return render_template("kiireellisyysluokat/list.html", kiireellisyysluokat = Kiireellisyysluokka.query.all())

@app.route("/kiireellisyysluokat/new/")
@login_required
def kiireellisyysluokat_form():
    return render_template("kiireellisyysluokat/new.html", form = KiireellisyysluokkaForm())

@app.route("/kiireellisyysluokat", methods=["POST"])
@login_required
def kiireellisyysluokat_create():
    form = KiireellisyysluokkaForm(request.form)

    if not form.validate():
        return render_template("kiireellisyysluokat/new.html", form = form)

    luokka = Kiireellisyysluokka(form.name.data,form.laakarit.data, form.sairaanhoitajat.data, form.perushoitajat.data)
    
    db.session().add(luokka)
    db.session().commit()
    return redirect(url_for("kiireellisyysluokat_index"))

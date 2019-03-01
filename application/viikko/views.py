from flask import render_template, request, redirect, url_for
from flask_login import current_user

from sqlalchemy import desc

from application import app, db, login_required
from application.viikko.models import Viikko
from application.paiva.models import Paiva
from application.viikko.forms import ViikkoForm


@app.route("/viikot", methods=["GET"])
@login_required(role="ANY")
def viikot_index():
    if current_user.job == 'ADMIN':
        return render_template("viikot/list.html", viikot = Viikko.query.all())
    else:
        return render_template("viikot/list.html", viikot = Viikko.get_viikot(current_user))
@app.route("/viikot/new/")
@login_required(role="ADMIN")
def viikot_form():
    return render_template("viikot/new.html", form = ViikkoForm())

@app.route("/viikot", methods=["POST"])
@login_required(role="ADMIN")
def viikot_create():
    form = ViikkoForm(request.form)

    if not form.validate():
        return render_template("viikot/new.html", form = form)

    viikko = Viikko(form.vuosi.data,form.numero.data)

    db.session().add(viikko)
    db.session().commit()

    Viikko.create_7_days(viikko)

    return redirect(url_for("viikot_index"))

@app.route("/viikot/delete/<int:id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def viikot_delete(id):
    viikko = Viikko.query.filter(Viikko.id==id).first()
    if viikko:
        db.session().delete(viikko)
        db.session().commit()
    return redirect(url_for("viikot_index"))

@app.route("/viikot/<int:id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def viikot_edit(id):
    viikko = Viikko.query.filter(Viikko.id==id).first()
    if viikko:
        form = ViikkoForm(request.form)
        if request.method == "POST" and form.validate():
            viikko.numero = form.numero.data
            viikko.vuosi = form.vuosi.data
            db.session().commit()
            return redirect(url_for("viikot_index"))
        return render_template("viikot/edit.html", form=form)
    else:
        return redirect(url_for("viikot_index"))

@app.route("/viikot/show/<int:id>", methods=["GET"])
@login_required(role="ANY")
def viikot_show(id):
    viikko = Viikko.query.filter(Viikko.id==id).first()
    paivat = viikko.paivat
    return render_template("viikot/show.html", viikko=viikko, paivat=paivat)
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import desc
from application import app, db
from application.viikko.models import Viikko
from application.viikko.forms import ViikkoForm


@app.route("/viikot", methods=["GET"])
@login_required
def viikot_index():
    return render_template("viikot/list.html", viikot = Viikko.query.order_by("vuosi desc").all())

@app.route("/viikot/new/")
@login_required
def viikot_form():
    return render_template("viikot/new.html", form = ViikkoForm())

@app.route("/viikot", methods=["POST"])
@login_required
def viikot_create():
    form = ViikkoForm(request.form)

    if not form.validate():
        return render_template("viikot/new.html", form = form)

    viikko = Viikko(form.vuosi.data,form.numero.data)
    viikko.account_id = current_user.id
    
    db.session().add(viikko)
    db.session().commit()
    return redirect(url_for("viikot_index"))
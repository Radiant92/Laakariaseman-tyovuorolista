from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.tunti.models import Tunti
from application.tunti.forms import TuntiForm

@app.route("/tunnit/show/<int:id>", methods=["GET"])
@login_required(role="ANY")
def tunnit_show(id):
    tunti = Tunti.query.filter(Tunti.id==id).first()
    return render_template("tunnit/show.html", tunti=tunti)

@app.route("/tunnit/<int:id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def tunnit_edit(id):
    tunti = Tunti.query.filter(Tunti.id==id).first()
    if tunti:
        form = TuntiForm(request.form)
        if request.method == "POST" and form.validate():  
            Tunti.set_luokka(tunti, form.luokka.data)
            return redirect(url_for("tunnit_show", id=tunti.id))
        return render_template("tunnit/edit.html", form=form)
    else:
        return redirect(url_for("tunnit_show", id=id))
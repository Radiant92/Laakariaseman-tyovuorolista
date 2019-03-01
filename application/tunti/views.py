from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.tunti.models import Tunti
from application.tunti.forms import TuntiForm, LisaaUserForm
from application.auth.models import User
from application.kiireellisyysluokka.models import Kiireellisyysluokka
def getLuokat():
    luokat = Kiireellisyysluokka.query.all()
    lista = []
    for i in luokat:
        ident = (str(i.id),i.name)
        lista.append(ident)
    return lista

def getUsers():
    users = User.query.filter(User.job !='ADMIN').all()
    lista = []
    for i in users:
        ident = (str(i.id),i.name + ', ' + i.job)
        lista.append(ident)
    return lista

def userOverflow(tunti):
    luokka = tunti.get_luokka()
    laakarit = 0
    sHoitajat = 0
    pHoitajat = 0
    for i in tunti.userit:
        if i.job == 'Lääkäri':
            laakarit += 1
        elif i.job == 'Sairaanhoitaja':
            sHoitajat += 1
        elif i.job == 'Perushoitaja':
            pHoitajat += 1
    laakarit -= luokka.laakarit
    if laakarit >= 0:
        sHoitajat += laakarit
        sHoitajat -= luokka.sairaanhoitajat
        if sHoitajat >= 0:
            pHoitajat += sHoitajat
            pHoitajat -= luokka.perushoitajat
            return pHoitajat
        return sHoitajat
    return laakarit


def checkTila(tunti):
    maara = tunti.userit.count()
    if tunti.get_luokka() is None:
        if maara == 0:
            tunti.tila = 0
        else:
            tunti.tila = maara
    else:
        tulos = userOverflow(tunti)
        if tulos == 0:
            tunti.tila = 1
        elif tulos > 0:
            tunti.tila = tulos +1
        else:
            tunti.tila = 0
    db.session().commit()


@app.route("/tunnit/show/<int:id>", methods=["GET"])
@login_required(role="ANY")
def tunnit_show(id):
    tunti = Tunti.query.filter(Tunti.id == id).first()
    return render_template("tunnit/show.html", tunti=tunti)


@app.route("/tunnit/<int:id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def tunnit_edit(id):
    tunti = Tunti.query.filter(Tunti.id == id).first()
    if tunti:
        form = TuntiForm(request.form)
        form.luokka.choices = getLuokat()
        if request.method == "POST" and form.validate():
            Tunti.set_luokka(tunti, form.luokka.data)
            checkTila(tunti)
            return redirect(url_for("tunnit_show", id=tunti.id))
        return render_template("tunnit/edit.html", form=form)
    else:
        return redirect(url_for("tunnit_show", id=id))


@app.route("/tunnit/lisaaUserit/<int:id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def tunnit_userit(id):
    tunti = Tunti.query.filter(Tunti.id == id).first()
    if tunti:
        form = LisaaUserForm(request.form)
        form.userit.choices = getUsers()
        if form.validate_on_submit():
            users = form.userit.data
            for i in users:
                ui = int(i)
                user = User.query.filter(User.id == ui).first()
                if user not in tunti.userit:
                    tunti.userit.append(user)
                db.session().commit()
            checkTila(tunti)
            return redirect(url_for("tunnit_show", id=tunti.id))
        return render_template("tunnit/userit.html", form=form)
    else:
        return redirect(url_for("tunnit_show", id=id))


@app.route("/tunnit/delete/<int:id>/<int:tunti_id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def tunti_user_delete(id, tunti_id):
    tunti = Tunti.query.filter(Tunti.id == tunti_id).first()
    user = User.query.filter(User.id == id).first()
    if tunti:
        tunti.userit.remove(user)
        db.session().commit()
        checkTila(tunti)
    return redirect(url_for("tunnit_show", id=tunti_id))

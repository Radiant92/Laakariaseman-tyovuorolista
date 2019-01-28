from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
  
from application import app, db
from application.auth.models import User
from application.auth.forms import UserForm
from application.auth.forms import LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "Virheellinen käyttäjätunnus tai salasana")
    login_user(user)
    return redirect(url_for("index"))   

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index")) 

@app.route("/employees", methods=["Get"])
def employees_index():
    return render_template("employees/list.html", employees = User.query.all())

@app.route("/employees/new/")
def employees_form():
    return render_template("employees/new.html", form = UserForm())

@app.route("/employees/<user_id>", methods=["POST"])
def employees_set_active(user_id):
    u = User.query.get(user_id)
    if u.active:
        u.active = False
    else:
        u.active = True
    
    db.session().commit()

    return redirect(url_for("employees_index"))

@app.route("/employees/", methods=["POST"])
def employees_create():
    form = UserForm(request.form)

    if not form.validate():
        return render_template("employees/new.html", form = form)

    u = User(form.name.data,form.username.data ,form.password.data, form.job.data)
    
    db.session().add(u)
    db.session().commit()
    return redirect(url_for("employees_index"))

from application import app, db
from flask import redirect, render_template, request, url_for
from application.employees.models import Employee

@app.route("/employees", methods=["Get"])
def employees_index():
    return render_template("employees/list.html", employees = Employee.query.all())

@app.route("/employees/new/")
def employees_form():
    return render_template("employees/new.html")

@app.route("/employees/<employee_id>", methods=["POST"])
def employees_set_active(employee_id):
    e = Employee.query.get(employee_id)

    if e.active:
        e.active = False
    else:
        e.active = True
    
    db.session().commit()

    return redirect(url_for("employees_index"))

@app.route("/employees/", methods=["POST"])
def employees_create():
    e = Employee(request.form.get("name"), request.form.get("password"), request.form.get("job"))
    
    db.session().add(e)
    db.session().commit()
    return redirect(url_for("employees_index"))

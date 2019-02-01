from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, PasswordField, Form
from wtforms import validators, ValidationError
from application.auth.models import User
class UserForm(FlaskForm):
    name = StringField("Nimi",[validators.length(min=3, max=30, message="nimen täytyy olla 3 - 30 merkkiä pitkä")])
    username = StringField("Käyttäjänimi",[validators.length(min=3, max=30, message="Käyttäjänimen täytyy olla 3 - 30 merkkiä pitkä")])
    password = PasswordField("Salasana",[validators.length(min=5, max=30, message="Salasanan tulee olla 5 - 30 merkkiä pitkä"), validators.EqualTo("confirm", message="Salasanat eivät täsmää")])
    confirm = PasswordField("Salasana uudelleen")
    job = SelectField(u"Ammatti", choices=[("Lääkäri","Lääkäri"),("Sairaanhoitaja","Sairaanhoitaja"),("Perushoitaja","Perushoitaja")])
    submit = SubmitField("Lisää työntekijä")
    
    class Meta:
        csrf = False

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Käyttäjänimi on jo käytössä!")

class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi")
    password = PasswordField("Salasana")
    submit = SubmitField("Kirjaudu sisään")
    class Meta:
        csrf = False
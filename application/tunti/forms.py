from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, Form
from wtforms import validators, ValidationError
from application.tunti.models import Tunti
from application.tuntiuser.models import TuntiUser
from application.auth.models import User
from application.kiireellisyysluokka.models import Kiireellisyysluokka


class TuntiForm(FlaskForm):
    luokat = Kiireellisyysluokka.query.all()
    lista = []
    for i in luokat:
        ident = (str(i.id),i.name)
        lista.append(ident)
    luokka = SelectField("valitse kiireellisyysluokka", choices=lista)
    submit = SubmitField("Vahvista")

    class Meta:
        csrf = False
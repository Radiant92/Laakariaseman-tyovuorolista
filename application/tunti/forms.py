from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, Form, SelectMultipleField, widgets
from wtforms import validators, ValidationError
from application.tunti.models import Tunti
from application.auth.models import User
from application.kiireellisyysluokka.models import Kiireellisyysluokka


class TuntiForm(FlaskForm):
    luokka = SelectField("valitse kiireellisyysluokka")
    submit = SubmitField("Vahvista")
    class Meta:
        csrf = False
        
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()
    class Meta:
        csrf = False


class LisaaUserForm(FlaskForm):

    userit = MultiCheckboxField(u"Valitse työntekijät")
    username = StringField("Vahvista allekirjoittamalla",[validators.length(min=3, max=30, message="allekirjoituksen täytyy olla 3 - 30 merkkiä pitkä")])
    submit = SubmitField("vahvista")
    class Meta:
        csrf = False


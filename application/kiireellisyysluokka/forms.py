from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Form, IntegerField
from wtforms import validators
class KiireellisyysluokkaForm(FlaskForm):
    name = StringField("Nimi",[validators.data_required(message="Luokalla täytyy olla nimi")])
    laakarit = IntegerField("Lääkärien määrä", [validators.NumberRange(min=0, message="Määrän tulee olla vähintään 0")])
    sairaanhoitajat = IntegerField("Lääkärien määrä", [validators.NumberRange(min=0, message="Määrän tulee olla vähintään 0")])
    perushoitajat = IntegerField("Lääkärien määrä", [validators.NumberRange(min=0, message="Määrän tulee olla vähintään 0")])
    class Meta:
        csrf = False
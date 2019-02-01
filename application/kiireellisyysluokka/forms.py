from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Form, IntegerField 
from wtforms import validators, ValidationError
from application.kiireellisyysluokka.models import Kiireellisyysluokka
class KiireellisyysluokkaForm(FlaskForm):
    name = StringField("Nimi",[validators.data_required(message="Luokalla täytyy olla nimi")])
    laakarit = IntegerField("Lääkärien määrä", [validators.NumberRange(min=0, message="Määrän tulee olla vähintään 0")])
    sairaanhoitajat = IntegerField("Sairaanhoitajien määrä", [validators.NumberRange(min=0, message="Määrän tulee olla vähintään 0")])
    perushoitajat = IntegerField("Perushoitajien määrä", [validators.NumberRange(min=0, message="Määrän tulee olla vähintään 0")])
    submit = SubmitField("valmis")

    def validate_name(self, name):
        luokka = Kiireellisyysluokka.query.filter_by(name=name.data).first()
        if luokka is not None:
            raise ValidationError("Tämän niminen kiireellisyysluokka on jo olemassa, ole hyvä ja valitse toinen nimi tai muokkaa jo olemassaolevaa.")

    class Meta:
        csrf = False

class KiireellisyysluokkaEditForm(FlaskForm):
    laakarit = IntegerField("Lääkärien määrä", [validators.NumberRange(min=0, message="Määrän tulee olla vähintään 0")])
    sairaanhoitajat = IntegerField("Sairaanhoitajien määrä", [validators.NumberRange(min=0, message="Määrän tulee olla vähintään 0")])
    perushoitajat = IntegerField("Perushoitajien määrä", [validators.NumberRange(min=0, message="Määrän tulee olla vähintään 0")])
    submit = SubmitField("muokkaa")
    class Meta:
        csrf = False
        
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, Form
from wtforms import validators, ValidationError
from datetime import datetime
from application.viikko.models import Viikko

class ViikkoForm(FlaskForm):
    vuosi = IntegerField("Vuosi", [validators.NumberRange(min=0, message="vuoden tulee olla vähintään 0")])
    numero = IntegerField("Viikon numero", [validators.NumberRange(min=1, max=52, message="luvun tulee olla välillä 1 ja 52")]) 
    submit = SubmitField("valmis")

    def validate_numero(self, numero):
        viikko = Viikko.query.filter_by(vuosi=self.vuosi.data, numero=numero.data).first()
        if viikko is not None:
            raise ValidationError("viikko on jo luotu! Mene viikkojen listaukseen ja valitse muokkaa viikon kohdalta")
    class Meta:
        csrf = False
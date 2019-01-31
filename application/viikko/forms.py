from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms import validators
from datetime import datetime

class ViikkoForm(FlaskForm):
    vuosi = IntegerField("Vuosi", [validators.NumberRange(min=0, message="vuoden tulee olla vähintään 0")])
    numero = IntegerField("Viikon numero", [validators.NumberRange(min=1, max=52, message="luvun tulee olla välillä 1 ja 52")]) 
    submit = SubmitField("valmis")
    class Meta:
        csrf = False
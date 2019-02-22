from application import db
from application.models import Base
from sqlalchemy.sql import text
from application.paiva.models import Paiva

class Viikko(Base):
    __tablename__ = "viikko"

    vuosi = db.Column(db.Integer, nullable=False)
    numero = db.Column(db.Integer, nullable=False)

    paivat = db.relationship("Paiva", backref='viikko', lazy=True, cascade="all, delete-orphan")

    def __init__(self, vuosi, numero):
        self.vuosi = vuosi
        self.numero = numero

    @staticmethod
    def create_7_days(self):
        maanantai = Paiva("maanantai")
        maanantai.viikko_id = self.id

        tiistai = Paiva("tiistai")
        tiistai.viikko_id = self.id

        keskiviikko = Paiva("keskiviikko")
        keskiviikko.viikko_id = self.id

        
        torstai = Paiva("torstai")
        torstai.viikko_id = self.id

        
        perjantai = Paiva("perjantai")
        perjantai.viikko_id = self.id

        
        lauantai = Paiva("lauantai")
        lauantai.viikko_id = self.id
        
        
        sunnuntai = Paiva("sunnuntai")
        sunnuntai.viikko_id = self.id


        db.session().add(maanantai)
        db.session().add(tiistai)
        db.session().add(keskiviikko)
        db.session().add(torstai)
        db.session().add(perjantai)
        db.session().add(lauantai)
        db.session().add(sunnuntai)
        db.session().commit()

        Paiva.create_24_hours(maanantai)
        Paiva.create_24_hours(tiistai)
        Paiva.create_24_hours(keskiviikko)
        Paiva.create_24_hours(torstai)
        Paiva.create_24_hours(perjantai)
        Paiva.create_24_hours(lauantai)
        Paiva.create_24_hours(sunnuntai)
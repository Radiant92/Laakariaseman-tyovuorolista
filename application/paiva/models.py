from application import db
from application.models import BaseTila
from application.tunti.models import Tunti
class Paiva(BaseTila):
    __tablename__ = "paiva"

    name = db.Column(db.String(144), nullable=False)
    tunnit = db.relationship("Tunti", backref='paiva', lazy=True, cascade="all, delete-orphan")
    viikko_id = db.Column(db.Integer, db.ForeignKey('viikko.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.tila = False 
    
    @staticmethod
    def create_24_hours(self):
        for i in range(0,24):
            p = Tunti(i)
            p.paiva_id = self.id
            db.session().add(p)
        db.session().commit()
from application import db
from application.models import Base
from application.kiireellisyysluokka.models import Kiireellisyysluokka
class Tunti(Base):
    __tablename__ = "tunti"

    tunti = db.Column(db.Integer, nullable=False)

    userit = db.relationship("TuntiUser", backref='tunti', lazy=True)
    
    paiva_id = db.Column(db.Integer, db.ForeignKey('paiva.id'), nullable=False)

    luokka_id = db.Column(db.Integer, db.ForeignKey('kiireellisyysluokka.id'), nullable=True)

    def __init__(self, tunti):
        self.tunti = tunti

    
    def get_luokka(self):
        luokka = Kiireellisyysluokka.query.filter(Kiireellisyysluokka.id==self.luokka_id).first()
        return luokka
    
    @staticmethod
    def set_luokka(self, lid):
        self.luokka_id = int(lid)
        db.session().commit()
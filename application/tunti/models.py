from application import db
from application.models import Base
from application.kiireellisyysluokka.models import Kiireellisyysluokka
from sqlalchemy import Table

tunti_user = Table('tunti_user', Base.metadata,
    db.Column('account_id', db.Integer, db.ForeignKey('account.id')),
    db.Column('tunti_id', db.Integer, db.ForeignKey('tunti.id')))

class Tunti(Base):
    __tablename__ = 'tunti'

    tunti = db.Column(db.Integer, nullable=False)

    userit = db.relationship('User', secondary=tunti_user, back_populates='tunnit', lazy='dynamic')
    
    paiva_id = db.Column(db.Integer, db.ForeignKey('paiva.id'), nullable=False)

    luokka_id = db.Column(db.Integer, db.ForeignKey('kiireellisyysluokka.id'), nullable=True)

    tila = db.Column(db.Integer, nullable=False)

    def __init__(self, tunti):
        self.tunti = tunti
        self.tila = 0

    
    def get_luokka(self):
        luokka = Kiireellisyysluokka.query.filter(Kiireellisyysluokka.id==self.luokka_id).first()
        return luokka
    
    @staticmethod
    def set_luokka(self, lid):
        self.luokka_id = int(lid)
        db.session().commit()
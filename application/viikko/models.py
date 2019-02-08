from application import db
from application.models import Base
from sqlalchemy.sql import text
class Viikko(Base):
    __tablename__ = "viikko"
   
    vuosi = db.Column(db.Integer, nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    
    paivat = db.relationship("Paiva", backref='viikko', lazy=True)

    def __init__(self, vuosi, numero):
        self.vuosi = vuosi
        self.numero = numero 

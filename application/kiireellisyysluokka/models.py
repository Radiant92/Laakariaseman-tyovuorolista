from application import db
from application.models import Base
class Kiireellisyysluokka(Base):
    __tablename__ = "kiireellisyysluokka"

    name = db.Column(db.String(144), nullable=False)
    laakarit = db.Column(db.Integer, nullable=False)
    sairaanhoitajat = db.Column(db.Integer, nullable=False)
    perushoitajat = db.Column(db.Integer, nullable=False)

    def __init__(self, name, laakarit, sairaanhoitajat, perushoitajat):
        self.name = name
        self.laakarit = laakarit
        self.sairaanhoitajat = sairaanhoitajat
        self.perushoitajat = perushoitajat 
from application import db
from application.models import BaseTila
class Paiva(BaseTila):
    __tablename__ = "paiva"

    name = db.Column(db.String(144), nullable=False)
    tunnit = db.relationship("Tunti", backref='paiva', lazy=True)
    viikko_id = db.Column(db.Integer, db.ForeignKey('viikko.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.tila = False
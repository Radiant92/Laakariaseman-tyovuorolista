from application import db
from application.models import BaseTila
class Tunti(BaseTila):
    __tablename__ = "tunti"

    tunti = db.Column(db.Integer, nullable=False)

    userit = db.relationship("TuntiUser", backref='tunti', lazy=True)
    
    paiva_id = db.Column(db.Integer, db.ForeignKey('paiva.id'), nullable=False)

    def __init__(self, tunti):
        self.tunti = tunti
        self.tila = False
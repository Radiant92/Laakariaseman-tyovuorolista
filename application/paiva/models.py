from application import db
from application.models import BaseTila
from application.tunti.models import Tunti
from sqlalchemy.sql import text
from application.auth.models import User
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

    def get_tunti(self, i):
        for tunti in self.tunnit:
            if tunti.tunti == i:
                return tunti

    def get_is_empty_for_user(self, user):
        stmt = text("SELECT account.id, paiva.id From paiva, tunti, tunti_user, account "
                    "WHERE paiva.id = tunti.paiva_id "
                    "AND tunti_user.tunti_id = tunti.id "
                    "AND account.id = tunti_user.account_id "
                    "GROUP BY account.id, paiva.id")
        res = db.engine.execute(stmt)
        for row in res:
            useri = User.query.filter(User.id == int(row[0])).first()
            if useri.username == user.username and self.id == int(row[1]):
                return True
        return False


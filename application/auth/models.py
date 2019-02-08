from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):
    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    job = db.Column(db.String(144), nullable=False)
    active = db.Column(db.Boolean(), nullable=False)
    hallinto = db.Column(db.Boolean(), nullable=False)

    tunnit = db.relationship("TuntiUser", backref='account', lazy=True)

    def __init__(self, name, username, password, job):
        self.name = name
        self.username = username
        self.password = password
        self.job = job
        self.active = True
        self.hallinto = True

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_admin(self):
        return self.hallinto

    @staticmethod
    def find_users_under_40_hours_work():
        stmt = text("SELECT Account.id, Account.job FROM Account"
                    " LEFT JOIN TuntiUser ON TuntiUser.account_id = Account.id"
                    " LEFT JOIN Tunti ON Tunti.id = TuntiUser.tunti_id"
                    " WHERE (NOT Account.job='admin' AND Tunti.tila IS null)"
                    " GROUP BY Account.id"
                    " HAVING COUNT(Tunti.id) < 40")

        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[0], "job":row[1]})

        return response
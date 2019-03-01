from application import db
from application.models import Base
from sqlalchemy.sql import text
from application.tunti.models import tunti_user


class User(Base):
    __tablename__ = 'account'

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    job = db.Column(db.String(144), nullable=False)
    active = db.Column(db.Boolean(), nullable=False)

    tunnit = db.relationship(
        'Tunti', secondary=tunti_user, back_populates="userit", lazy='dynamic')

    def __init__(self, name, username, password, job):
        self.name = name
        self.username = username
        self.password = password
        self.job = job
        self.active = True

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_admin(self):
        if(self.job == "ADMIN"):
            return True
        else:
            return False

    def roles(self):
        return [self.job]


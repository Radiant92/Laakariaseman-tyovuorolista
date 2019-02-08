from application import db
from application.models import Base
class TuntiUser(Base):
    __tablename__ = "tuntiuser"

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)    
    tunti_id = db.Column(db.Integer, db.ForeignKey('tunti.id'), nullable=False) 

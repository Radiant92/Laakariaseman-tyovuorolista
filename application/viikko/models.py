from application import db
from application.models import Base
from sqlalchemy.sql import text
from application.paiva.models import Paiva

class Viikko(Base):
    __tablename__ = "viikko"

    vuosi = db.Column(db.Integer, nullable=False)
    numero = db.Column(db.Integer, nullable=False)

    paivat = db.relationship("Paiva", backref='viikko', lazy=True, cascade="all, delete-orphan")

    def __init__(self, vuosi, numero):
        self.vuosi = vuosi
        self.numero = numero

    @staticmethod
    def create_7_days(self):
        maanantai = Paiva("maanantai")
        maanantai.viikko_id = self.id

        tiistai = Paiva("tiistai")
        tiistai.viikko_id = self.id

        keskiviikko = Paiva("keskiviikko")
        keskiviikko.viikko_id = self.id

        
        torstai = Paiva("torstai")
        torstai.viikko_id = self.id

        
        perjantai = Paiva("perjantai")
        perjantai.viikko_id = self.id

        
        lauantai = Paiva("lauantai")
        lauantai.viikko_id = self.id
        
        
        sunnuntai = Paiva("sunnuntai")
        sunnuntai.viikko_id = self.id


        db.session().add(maanantai)
        db.session().add(tiistai)
        db.session().add(keskiviikko)
        db.session().add(torstai)
        db.session().add(perjantai)
        db.session().add(lauantai)
        db.session().add(sunnuntai)
        db.session().commit()

        Paiva.create_24_hours(maanantai)
        Paiva.create_24_hours(tiistai)
        Paiva.create_24_hours(keskiviikko)
        Paiva.create_24_hours(torstai)
        Paiva.create_24_hours(perjantai)
        Paiva.create_24_hours(lauantai)
        Paiva.create_24_hours(sunnuntai)
    @staticmethod
    def get_viikot(user):
        stmt = text("SELECT count(tunti.id), viikko.id, account.username "
		            "From viikko, paiva, tunti, tunti_user, account "
                    "WHERE viikko.id = paiva.viikko_id "
                    "AND paiva.id = tunti.paiva_id "
                    "AND tunti_user.tunti_id = tunti.id "
                    "AND account.id = tunti_user.account_id "
		            "AND tunti.tila > 0 "
		            "GROUP BY viikko.id, account.username")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            if row[2] == user.username:
                vid = int(row[1])
                viikko = Viikko.query.filter(Viikko.id == vid).first()
                response.append({"viikko":viikko, "tunteja":row[0]})
        return response

    @staticmethod
    def find_overflow():
        stmt = text("SELECT distinct viikko.id, count(tunti.id) FROM  tunti, paiva, viikko "
                    "WHERE viikko.id = paiva.viikko_id "
                    "AND paiva.id = tunti.paiva_id "
                    "AND tunti.tila > 1 "
                    "GROUP BY viikko.id "
                    "ORDER BY viikko.id")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            viikko = Viikko.query.filter(Viikko.id == int(row[0])).first()
            response.append({"vuosi":viikko.vuosi ,"numero":viikko.numero, "over":row[1]})
        return response

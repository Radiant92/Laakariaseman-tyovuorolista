from application import db

class Kiireellisyysluokka(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


    name = db.Column(db.String(144), nullable=False)
    laakarit = db.Column(db.Integer, nullable=False)
    sairaanhoitajat = db.Column(db.Integer, nullable=False)
    perushoitajat = db.Column(db.Integer, nullable=False)

    def __init__(self, name, laakarit, sairaanhoitajat, perushoitajat):
        self.name = name
        self.laakarit = laakarit
        self.sairaanhoitajat = sairaanhoitajat
        self.perushoitajat = perushoitajat
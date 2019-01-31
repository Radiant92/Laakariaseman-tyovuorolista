from application import db

class User(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    job = db.Column(db.String(144), nullable=False)
    active = db.Column(db.Boolean(), nullable=False)
    hallinto = db.Column(db.Boolean(), nullable=False)

    viikot = db.relationship("Viikko", backref='account', lazy=True)

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
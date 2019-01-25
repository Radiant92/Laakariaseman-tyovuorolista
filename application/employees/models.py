from application import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    job = db.Column(db.String(144), nullable=False)
    active = db.Column(db.Boolean(), nullable=False)
    def __init__(self, name, password, job):
        self.name = name
        self.password = password
        self.job = job
        self.active = True

from . import db

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    batch_no = db.Column(db.String(50), nullable=False)
    linkedin_url = db.Column(db.String, nullable=True)


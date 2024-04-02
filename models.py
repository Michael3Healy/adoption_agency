from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, nullable=False)

    species = db.Column(db.Text, nullable=False)

    photo_url = db.Column(db.Text, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5TpeZd7wGc3-bJqu1p1GkKCgi46gPjHJgRA&s')

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean, nullable=False, default=True)
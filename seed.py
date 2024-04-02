from models import db, Pet
from app import app

db.drop_all()
db.create_all()

bowser = Pet(name='Bowser', species='Turtle', age=10, notes='Highly Irritable', photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYFUy7E0CDruPtRlAh_BYERn46N6NpOD_zvg&s')
whiskey = Pet(name='Whiskey', species='Dog')

db.session.add_all([bowser, whiskey])
db.session.commit()


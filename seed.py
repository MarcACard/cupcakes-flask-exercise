from models import db, Cupcake
from app import app

db.drop_all()
db.create_all()

c1 = Cupcake(flavor="Chocolate", size="Regular", rating=4)
c2 = Cupcake(flavor="Vanila", size="Regular", rating=5)
c3 = Cupcake(flavor="Birthday Cake", size="Large", rating=4)
c4 = Cupcake(flavor="Strawberry Shortcake", size="Small", rating=1)

db.session.add_all([c1, c2, c3, c4])
db.session.commit()

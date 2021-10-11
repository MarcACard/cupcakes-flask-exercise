from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect DB to App"""
    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """Cupcake Model"""

    __tablename__ = "cupcake"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(
        db.String, nullable=False, default="https://tinyurl.com/demo-cupcake"
    )

    def __repr__(self):
        return f"<Cupcake {self.flavor}>"

    def serialize(self):
        """Serialize a Cupcake SQLAlchemy obj to a dictionary."""
        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image,
        }

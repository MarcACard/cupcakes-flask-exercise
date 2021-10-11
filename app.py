from flask import Flask, jsonify, request
from flask.templating import render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcake"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

connect_db(app)


#########################
# === FRONTEND Routes ===
#########################
@app.route("/")
def home():
    """Render Homepage of Site."""
    return render_template("home.html")


####################
# === API ROUTES ===
####################


@app.route("/api/cupcakes")
def get_cupcakes():
    """Return all cupcakes in JSON"""
    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcakes():
    """Create a new cupcake"""

    if request.json["image"]:
        cupcake = Cupcake(
            flavor=request.json["flavor"],
            size=request.json["size"],
            rating=request.json["rating"],
            image=request.json["image"],
        )
    else:
        cupcake = Cupcake(
            flavor=request.json["flavor"],
            size=request.json["size"],
            rating=request.json["rating"],
        )

    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.serialize()), 201)


@app.route("/api/cupcakes/<int:id>")
def get_cupcake(id):
    """Return a JSON of a cupcake or 404 if it doesn't exist."""
    cupcake = Cupcake.query.get_or_404(id)

    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes/<int:id>", methods=["PATCH"])
def update_cupcake(id):
    """Update aspects of a cupcake defined by the json payload."""

    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes/<int:id>", methods=["DELETE"])
def delete_cupcake(id):
    """Delete a Cupcake from the DB."""
    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify({"message": "Deleted"})

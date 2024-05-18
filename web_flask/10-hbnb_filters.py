#!/usr/bin/python3
""" Here goes every thing """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filter():
    """ """
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)

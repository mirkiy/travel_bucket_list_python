from flask import Flask, render_template
from flask import Blueprint
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository


cities_blueprint = Blueprint("cities", __name__)


# homepage route
# GET '/to visit'
@cities_blueprint.route("/to_visit")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html")

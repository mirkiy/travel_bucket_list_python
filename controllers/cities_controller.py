from flask import Flask, render_template, request, redirect
from flask import Blueprint
from werkzeug.utils import redirect
from models.city import City
# from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)


# index route
# GET '/cities'
@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities=cities)

# GET '/cities/new_city'


@cities_blueprint.route("/cities/new_city", methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template("cities/new_city.html", all_countries=countries)


# CREATE
# POST '/cities'
@cities_blueprint.route("/cities", methods=['POST'])
def create_new_city():
    country_id = request.form['country_id']
    name = request.form['name']
    population = request.form['population']
    review = request.form['review']
    sights = request.form['sights']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(country, name, population, review, sights, visited)
    city_repository.save(city)
    return redirect('/cities')

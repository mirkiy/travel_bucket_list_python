from flask import Flask, render_template, request, redirect
from flask import Blueprint
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

# EDIT
# GET '/cities/<id>/edit'


@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template('cities/edit.html', city=city, all_countries=countries)

# UPDATE
# UPDATE 'cities/<id>'


@cities_blueprint.route("/cities/<id>/edit", methods=['POST'])
def update_city(id):
    country_id = request.form['country_id']
    name = request.form['name']
    population = request.form['population']
    review = request.form['review']
    sights = request.form['sights']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(country, name, population, review, sights, visited, id)
    city_repository.update(city)
    return redirect('/cities')

# DELETE
# DELETE '/cities/<id>'


@cities_blueprint.route("/cities/<id>/delete", methods=["POST"])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities')

# show only visited cities
# GET '/cities/visited'


@cities_blueprint.route("/cities/visited")
def visited_cities():
    cities = city_repository.select_all_visited()
    return render_template("cities/visited.html", all_cities=cities)

# show not visited cities
# GET '/cities/to_visit


@cities_blueprint.route("/cities/to_visit")
def to_visit_cities():
    cities = city_repository.select_to_visit()
    return render_template("cities/to_visit.html", all_cities=cities)

from flask import Flask, render_template
from flask import Blueprint
from models.country import Country

import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)


# index route
# GET '/countries'
@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries=countries)

# GET 'countries/new_country'
@countries_blueprint.route("/countries/new_country", methods=['GET'])
def new_country():
    countries = country_repository.select_all()
    return render_template("countries/new_country.html", all_countries=countries)

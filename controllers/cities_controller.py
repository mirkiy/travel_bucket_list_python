from flask import Flask, render_template
from flask import Blueprint
from models.city import City

import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

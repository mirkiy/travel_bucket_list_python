from flask import Flask, render_template
from flask import Blueprint
from models.country import Country

import repositories.country_repository as country_repository

country_blueprint = Blueprint("countries", __name__)

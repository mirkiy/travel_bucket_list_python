from db.run_sql import run_sql

from models.city import City
from models.country import Country
import repositories.country_repository as country_repository


def save(city):
    sql = "INSERT INTO cities (country_id, name, population, review, sights) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [city.country.id, city.name,
              city.population, city.review, city.sights]
    results = run_sql(sql, values)
    city.id = results[0]['id']
    return city


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(country, row['name'],
                    row['population'], row['review'], row["sights"], row['id'])
        cities.append(city)
    return cities


def select(id):
    city = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(result['country_id'])
        city = City(country, result['name'],
                    result['population'], result['review'], result["sights"], result['id'])
    return city

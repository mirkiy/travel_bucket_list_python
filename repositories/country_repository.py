from db.run_sql import run_sql

from models.country import Country
from models.city import City


def save(country):
    sql = "INSERT INTO countries (name, capital) VALUES (%s, %s) RETURNING *"
    values = [country.name, country.capital]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country


def select_all():
    countries = []

    sql = "SELECT * FROM countries ORDER BY name"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['capital'], row['id'])
        countries.append(country)
    return countries


def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id =%s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['capital'], result['id'])
    return country


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(country):
    sql = "UPDATE countries SET (name, capital) = (%s, %s) WHERE id =%s"
    values = [country.name, country.capital, country.id]
    run_sql(sql, values)


def cities(country):
    cities = []

    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['country_id'], row['name'],
                    row['population'], row['review'], row['sight'], row['visited'], row['id'])
        cities.append(city)
    return cities

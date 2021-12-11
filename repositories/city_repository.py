from db.run_sql import run_sql

from models.city import City
from models.country import Country
import repositories.country_repository as country_repository


def save(city):
    sql = "INSERT INTO cities (country_id, name, population, review, sights, visited) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [city.country.id, city.name,
              city.population, city.review, city.sights,city.visited]
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
                    row['population'], row['review'], row["sights"], row['visited'],row['id'])
        cities.append(city)
    return cities


def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(result['country_id'])
        city = City(country, result['name'],
                    result['population'], result['review'], result["sights"],result['visited'], result['id'])
    return city


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(city):
    sql = "UPDATE cities SET (country_id, name, population, review, sights) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [city.country.id, city.name,
              city.population, city.review, city.sights,city.visited, city.id]
    # print(values)
    run_sql(sql, values)

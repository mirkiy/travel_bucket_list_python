import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository


city_repository.delete_all()
country_repository.delete_all()

country1 = Country("Slovakia", "Bratislava")
country_repository.save(country1)
country2 = Country("Sweden", "Stockholm")
country_repository.save(country2)

# country_repository.select_all()

city1 = City(country1, "Trnava", 70000, 4,
             "lovely historical city centre", False)
city_repository.save(city1)


city2 = City(country2, "Stockholm", 700000, 4, "folk museum - skansen", False)
city_repository.save(city2)

# country, name, population, review, sights, visited
pdb.set_trace()

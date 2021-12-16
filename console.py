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
country3 = Country("United Kingdom", "London")
country_repository.save(country3)
country4 = Country("Germany", "Berlin")
country_repository.save(country4)
country5 = Country("Vietnam", "Hanoi")
country_repository.save(country5)
country6 = Country("Cuba", "Havana")
country_repository.save(country6)
country7 = Country("Italy", "Rome")
country_repository.save(country7)

city1 = City(country1, "Trnava", 70000, 4,
             "lovely historical city centre", False)
city_repository.save(city1)

city2 = City(country2, "Stockholm", 970000, 4, "folk museum - skansen", True)
city_repository.save(city2)

city3 = City(country3, "Gothenburgh", 570000, 3, "annual film festival", False)
city_repository.save(city3)

city4 = City(country6, "Santiago de Cuba", 433000, 4,
             "cultural life, Bacardi", False)
city_repository.save(city4)

city5 = City(country7, "Palermo", 673000, 3,
             "authentic Sicilian street-food", True)
city_repository.save(city5)

city6 = City(country7, "Naples", 2180000, 5, "pizza, close to Pompeii", True)
city_repository.save(city6)

city7 = City(country5, "Hanoi", 4870000, 5,
             "one of the most ancient capitals in the world", False)
city_repository.save(city7)


pdb.set_trace()

class City:

    def __init__(self, country, name, population, review, sights, visited,id=None):
        self.country = country
        self.name = name
        self.population = population
        self.review = review
        self.sights = sights
        self.visited = visited
        self.id = id

def mark_visited(self):
    self.visited = True
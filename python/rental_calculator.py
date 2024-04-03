class RentalCalculation():

    def __init__(self, movie_registry):
        self.movie_registry = movie_registry
        self.rentals = []
    
    def rent_movie(self, title, days):
        movie = self.movie_registry.get_movie(title)
        self.rentals.append(Rental(movie, days))

    def get_fee(self):
        fee = 0
        for rental in self.rentals:
            fee += rental.get_fee()
        return fee
    
    def get_points(self):
        points = 0
        for rental in self.rentals:
            points += rental.get_points()
        return points


class Rental():
    def __init__(self, movie, days):
        self.movie = movie
        self.days = days
    
    def get_fee(self):
        return self.movie.get_fee(self.days)
    
    def get_points(self):
        return self.movie.get_points(self.days)
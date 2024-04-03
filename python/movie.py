from abc import ABC, abstractmethod
from enum import Enum

MovieType = Enum('MovieType', ['REGULAR', 'CHILDREN'])

class Movie(ABC):

    def __init__(self, title, movie_type):
        self.title = title
        self.movie_type = movie_type

    @abstractmethod
    def get_fee(self):
        pass

    @abstractmethod
    def get_points(self):
        pass

class RegularMovie(Movie):
    def __init__(self, title):
        super().__init__(title, MovieType.REGULAR)
    
    def get_fee(self, days):
        return self.apply_free_days(days, 150)
    
    def get_points(self, days):
        return self.apply_free_days(days, 1)

    def apply_free_days(self, days, amount):
        if days < 3:
            return amount
        return amount + (days - 3) * amount


class ChildrenMovie(Movie):
    def __init__(self, title):
        super().__init__(title, MovieType.CHILDREN)
    
    def get_fee(self, days):
        return 100 * days
    
    def get_points(self, days):
        return 1

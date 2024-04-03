import pytest
from movies_registry import MovieRegistry
from rental_calculator import RentalCalculation
from movie import MovieType

@pytest.fixture
def movie_registry():
    registry = MovieRegistry()
    registry.add_movie("normal", MovieType.REGULAR)
    registry.add_movie("children", MovieType.CHILDREN)
    return registry

@pytest.fixture
def rental_calculation(movie_registry):
    return RentalCalculation(movie_registry)

def test_rent_normal_movie_1_day(rental_calculation):
    rental_calculation.rent_movie("normal", 1)
    assert 150 == rental_calculation.get_fee()
    assert 1 == rental_calculation.get_points()

def test_rent_normal_movie_2_days(rental_calculation):
    rental_calculation.rent_movie("normal", 2)
    assert 150 == rental_calculation.get_fee()
    assert 1 == rental_calculation.get_points()

def test_rent_normal_movie_3_days(rental_calculation):
    rental_calculation.rent_movie("normal", 3)
    assert 150 == rental_calculation.get_fee()
    assert 1 == rental_calculation.get_points()

def test_rent_normal_movie_4_days(rental_calculation):
    rental_calculation.rent_movie("normal", 4)
    assert 300 == rental_calculation.get_fee()
    assert 2 == rental_calculation.get_points()

def test_rent_normal_movie_5_days(rental_calculation):
    rental_calculation.rent_movie("normal", 5)
    assert 450 == rental_calculation.get_fee()
    assert 3 == rental_calculation.get_points()

def test_rent_children_movie_1_day(rental_calculation):
    rental_calculation.rent_movie("children", 1)
    assert 100 == rental_calculation.get_fee()
    assert 1 == rental_calculation.get_points()

def test_rent_children_movie_2_days(rental_calculation):
    rental_calculation.rent_movie("children", 2)
    assert 200 == rental_calculation.get_fee()
    assert 1 == rental_calculation.get_points()

def test_rent_children_movie_3_days(rental_calculation):
    rental_calculation.rent_movie("children", 3)
    assert 300 == rental_calculation.get_fee()
    assert 1 == rental_calculation.get_points()

def test_rent_2_normal_movies_1_day(rental_calculation):
    rental_calculation.rent_movie("normal", 1)
    assert 150 == rental_calculation.get_fee()
    assert 1 == rental_calculation.get_points()
    rental_calculation.rent_movie("normal", 1)
    assert 300 == rental_calculation.get_fee()
    assert 2 == rental_calculation.get_points()

def test_rent_2_normal_movies_2_days(rental_calculation):
    rental_calculation.rent_movie("normal", 2)
    assert 150 == rental_calculation.get_fee()
    assert 1 == rental_calculation.get_points()
    rental_calculation.rent_movie("normal", 2)
    assert 300 == rental_calculation.get_fee()
    assert 2 == rental_calculation.get_points()

def test_rent_2_normal_movies_3_days(rental_calculation):
    rental_calculation.rent_movie("normal", 3)
    assert 150 == rental_calculation.get_fee()
    assert 1 == rental_calculation.get_points()
    rental_calculation.rent_movie("normal", 3)
    assert 300 == rental_calculation.get_fee()
    assert 2 == rental_calculation.get_points()

def test_rent_2_normal_movies_4_days(rental_calculation):
    rental_calculation.rent_movie("normal", 4)
    assert 300 == rental_calculation.get_fee()
    assert 2 == rental_calculation.get_points()
    rental_calculation.rent_movie("normal", 4)
    assert 600 == rental_calculation.get_fee()
    assert 4 == rental_calculation.get_points()

def test_rent_normal_movie_and_children_movie_1_day(rental_calculation):
    rental_calculation.rent_movie("normal", 1)
    assert 150 == rental_calculation.get_fee()
    assert 1 == rental_calculation.get_points()
    rental_calculation.rent_movie("children", 1)
    assert 250 == rental_calculation.get_fee()
    assert 2 == rental_calculation.get_points()

def test_rent_normal_movie_and_children_movie_2_days(rental_calculation):
    rental_calculation.rent_movie("normal", 2)
    assert 150 == rental_calculation.get_fee()
    assert 1 == rental_calculation.get_points()
    rental_calculation.rent_movie("children", 2)
    assert 350 == rental_calculation.get_fee()
    assert 2 == rental_calculation.get_points()

def test_rent_normal_movie_and_children_movie_3_days(rental_calculation):
    rental_calculation.rent_movie("normal", 3)
    assert 150 == rental_calculation.get_fee()
    assert 1 == rental_calculation.get_points()
    rental_calculation.rent_movie("children", 3)
    assert 450 == rental_calculation.get_fee()
    assert 2 == rental_calculation.get_points()

def test_rent_normal_movie_and_children_movie_4_days(rental_calculation):
    rental_calculation.rent_movie("normal", 4)
    assert 300 == rental_calculation.get_fee()
    assert 2 == rental_calculation.get_points()
    rental_calculation.rent_movie("children", 4)
    assert 700 == rental_calculation.get_fee()
    assert 3 == rental_calculation.get_points()
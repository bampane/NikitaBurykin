import pytest
import random

from src.Circle import Circle
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Square import Square


@pytest.fixture
def def_rand_circle():
    circle = Circle(raidus=random.randrange(100))
    yield circle
    del circle


@pytest.fixture
def def_triangle():
    triangle = Triangle(13, 14, 15)
    yield triangle
    del triangle


@pytest.fixture
def def_rand_square():
    square = Square(random.randrange(100))
    yield square
    del square


@pytest.fixture
def def_rand_rectangle():
    rectangle = Rectangle(random.randrange(100), random.randrange(100))
    yield rectangle
    del rectangle

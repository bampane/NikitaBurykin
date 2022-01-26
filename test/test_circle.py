from src.Circle import Circle
from math import pi
import random

#Положительные кейсы
def test_cre_circle(def_rand_circle):
    assert def_rand_circle.name == 'Circle'

def test_circe_area():
    t_rad = random.randrange(100)
    t_circe_1 = Circle(raidus=t_rad)
    assert t_circe_1.area == t_rad * t_rad * pi

def test_circle_perimeter():
    t_rad=random.randrange(100)
    t_circe_1=Circle(raidus=t_rad)
    assert t_circe_1.perimeter==t_rad*2*pi


def test_circle_add_triangle(def_rand_circle,def_triangle):
    assert def_rand_circle.add_area(def_triangle)==(def_rand_circle.area+def_triangle.area)


def test_circle_add_square(def_rand_circle,def_rand_square):
    assert def_rand_circle.add_area(def_rand_square)==(def_rand_circle.area+def_rand_square.area)


def test_circle_add_circle(def_rand_circle):
    assert def_rand_circle.add_area(def_rand_circle)==(def_rand_circle.area+def_rand_circle.area)


def test_circle_add_rectangle(def_rand_circle,def_rand_rectangle):
    assert def_rand_circle.add_area(def_rand_rectangle) == (def_rand_circle.area + def_rand_rectangle.area)

#Негативные кейсы
def test_cre_negative():
    try:
        Circle(raidus=-1)
        assert False
    except Exception:
        assert True

def test_circle_add_negative(def_rand_circle):
    try:
        def_rand_circle.add_area(10)
        assert False
    except Exception:
        assert True
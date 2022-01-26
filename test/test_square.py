from src.Square import Square

import random

#Положительные кейсы
def test_cre_square(def_rand_square):
    assert def_rand_square.name == 'Square'

def test_square_area():
    t_side = random.randrange(100)
    t_square_1 = Square(t_side)
    assert t_square_1.area == t_side * t_side

def test_square_perimeter():
    t_side = random.randrange(100)
    t_square_1 = Square(t_side)
    assert t_square_1.perimeter==t_side*4


def test_square_add_triangle(def_rand_square,def_triangle):
    assert def_rand_square.add_area(def_triangle)==(def_rand_square.area+def_triangle.area)


def test_square_add_square(def_rand_square):
    assert def_rand_square.add_area(def_rand_square)==(def_rand_square.area+def_rand_square.area)


def test_square_add_circle(def_rand_square,def_rand_circle):
    assert def_rand_square.add_area(def_rand_circle)==(def_rand_square.area+def_rand_circle.area)


def test_square_add_rectangle(def_rand_square,def_rand_rectangle):
    assert def_rand_square.add_area(def_rand_rectangle) == (def_rand_square.area + def_rand_rectangle.area)

#Негативные кейсы
def test_cre_negative():
    try:
        Square(-10)
        assert False
    except Exception:
        assert True

def test_square_add_negative(def_rand_square):
    try:
        def_rand_square.add_area(10)
        assert False
    except Exception:
        assert True
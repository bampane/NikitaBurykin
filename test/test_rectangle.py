from src.Rectangle import Rectangle
import random

#Положительные кейсы
def test_cre_rectangle(def_rand_rectangle):
    assert def_rand_rectangle.name == 'Rectangle'

def test_rectangle_area():
    t_side_a = random.randrange(100)
    t_side_b = random.randrange(100)
    t_rect_1 = Rectangle(side_b=t_side_b,side_a=t_side_a)
    assert t_rect_1.area == t_side_a * t_side_b

def test_rectangle_perimeter():
    t_side_a = random.randrange(100)
    t_side_b = random.randrange(100)
    t_rect_1 = Rectangle(side_b=t_side_b, side_a=t_side_a)
    assert t_rect_1.perimeter==2*(t_side_a+t_side_b)


def test_rectangle_add_triangle(def_rand_rectangle,def_triangle):
    assert def_rand_rectangle.add_area(def_triangle)==(def_rand_rectangle.area+def_triangle.area)


def test_rectangle_add_square(def_rand_rectangle,def_rand_square):
    assert def_rand_rectangle.add_area(def_rand_square)==(def_rand_rectangle.area+def_rand_square.area)


def test_rectangle_add_circle(def_rand_rectangle,def_rand_circle):
    assert def_rand_rectangle.add_area(def_rand_circle)==(def_rand_rectangle.area+def_rand_circle.area)


def test_rectangle_add_rectangle(def_rand_rectangle):
    assert def_rand_rectangle.add_area(def_rand_rectangle) == (def_rand_rectangle.area + def_rand_rectangle.area)

#Негативные кейсы
def test_cre_negative_side_a():
    try:
        Rectangle(side_a=-10,side_b=10)
        assert False
    except Exception:
        assert True

def test_cre_negative_side_b():
    try:
        Rectangle(side_a=10,side_b=-10)
        assert False
    except Exception:
        assert True

def test_cre_negative():
    try:
        Rectangle(side_a=-10,side_b=-10)
        assert False
    except Exception:
        assert True

def test_rectangle_add_negative(def_rand_rectangle):
    try:
        def_rand_rectangle.add_area(10)
        assert False
    except Exception:
        assert True
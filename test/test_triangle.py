from src.Triangle import Triangle
from math import sqrt



#Положительные кейсы
def test_cre_triangle(def_triangle):
    assert def_triangle.name == 'Triangle'

def test_triangle_area():
    t_side_a = 16
    t_side_b = 17
    t_side_c = 18
    t_triangle=Triangle(t_side_a,t_side_b,t_side_c)
    p = (t_side_a + t_side_b + t_side_c) / 2
    assert t_triangle.area == sqrt(p * (p - t_side_a) * (p - t_side_b) * (p - t_side_c))

def test_triangle_perimeter():
    t_side_a = 16
    t_side_b = 17
    t_side_c = 18
    t_triangle=Triangle(t_side_a,t_side_b,t_side_c)
    assert t_triangle.perimeter==t_side_a+t_side_b+t_side_c


def test_triangle_add_triangle(def_triangle):
    assert def_triangle.add_area(def_triangle)==(def_triangle.area+def_triangle.area)


def test_triangle_add_square(def_triangle,def_rand_square):
    assert def_triangle.add_area(def_rand_square)==(def_triangle.area+def_rand_square.area)


def test_triangle_add_circle(def_triangle,def_rand_circle):
    assert def_triangle.add_area(def_rand_circle)==(def_triangle.area+def_rand_circle.area)


def test_triangle_add_rectangle(def_triangle,def_rand_rectangle):
    assert def_triangle.add_area(def_rand_rectangle) == (def_triangle.area + def_rand_rectangle.area)

#Негативные кейсы
def test_cre_negative():
    try:
        Triangle(1,2,3)
        assert False
    except Exception:
        assert True

def test_triangle_add_negative(def_triangle):
    try:
        def_triangle.add_area(10)
        assert False
    except Exception:
        assert True
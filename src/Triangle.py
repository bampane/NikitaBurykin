from src.Figure import Figure
from math import sqrt


class Triangle(Figure):
    __side_a = 0
    __side_b = 0
    __side_c = 0

    def __init__(self, side_a, side_b, side_c):
        if ((side_a + side_b) > side_c) and ((side_a + side_b) > side_c) and ((side_b + side_c) > side_a):
            self.name = "Triangle"
            self.__side_a = side_a
            self.__side_b = side_b
            self.__side_c = side_c
            p = (self.__side_a + self.__side_b + self.__side_c) / 2
            self._area = sqrt(p * (p - self.__side_a) * (p - self.__side_b) * (p - self.__side_c))
            self._perimeter = self.__side_a + self.__side_b + self.__side_c
        else:
            raise Exception("Impossible triangle")

    @property
    def area(self):
        return (self._area)

    @property
    def perimeter(self):
        return (self._perimeter)

from src.Figure import Figure
from math import sqrt

class Triangle(Figure):
    __side_a=0
    __side_b=0
    __side_c=0

    def __init__(self,side_a,side_b,side_c):
        self.name="Triangle"
        self.__side_a=side_a
        self.__side_b = side_b
        self.__side_c = side_c
        #Добавить проверку на невозможность создания треугольника#
    @property
    def area(self):
        p= (self.__side_a + self.__side_b + self.__side_c) / 2
        self._area=sqrt(p * (p - self.__side_a) * (p - self.__side_b) * (p - self.__side_c))
        return (self._area)

    @property
    def perimeter(self):
        self._perimetert= self.__side_a + self.__side_b + self.__side_c
        return (self._perimetert)
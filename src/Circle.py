from src.Figure import Figure
from math import pi


class Circle(Figure):
    __radius = 0

    def __init__(self, raidus):
        if raidus > 0:
            self.name = "Circle"
            self.__radius = raidus
            self._area = self.__radius * self.__radius * pi
            self._perimeter = self.__radius * 2 * pi
        else:
            raise Exception("Radius must be more that zero")


    @property
    def area(self):
        return (self._area)

    @property
    def perimeter(self):
        return (self._perimeter)

from src.Figure import Figure
from math import pi

class Circle(Figure):
    __radius=0

    def __init__(self,raidus):
        self.name="Circle"
        self.__radius=raidus
    @property
    def area(self):
        self._area= self.__radius * self.__radius * pi
        return (self.__area)

    @property
    def perimeter(self):
        self.__perimetert= self.__radius * 2 * pi
        return (self.__perimetert)
    def __repr__(self):
        return "({}){}:{}$:{}".format(self.name,self.__radius, self.__perimetert, self.__area)

a=Circle(10)
a.perimeter
a.area
print(a)
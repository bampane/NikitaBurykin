from src.Figure import Figure

class Rectangle(Figure):
    __side_a=0
    __side_b=0

    def __init__(self,side_a,side_b):
        self.name="Rectangle"
        self.__side_a=side_a
        self.__side_b=side_b
    @property
    def area(self):
        self._area= self.__side_a * self.__side_b
        return (self._area)

    @property
    def perimeter(self):
        self._perimetert=2*(self.__side_a + self.__side_b)
        return (self._perimetert)
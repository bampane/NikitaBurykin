from src.Figure import Figure

class Square(Figure):
    __side=0

    def __init__(self,side):
        self.name="Square"
        self.__side=side
    @property
    def area(self):
        self._area=self.__side*self.__side
        return (self._area)

    @property
    def perimeter(self):
        self._perimetert=self.__side*4
        return (self._perimetert)

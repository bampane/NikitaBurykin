from src.Figure import Figure


class Square(Figure):
    __side = 0

    def __init__(self, side):
        if side > 0:
            self.name = "Square"
            self.__side = side
            self._area = self.__side * self.__side
            self._perimeter = self.__side * 4
        else:
            raise Exception("SIDE LESS THEN ZERO")

    @property
    def area(self):
        return (self._area)

    @property
    def perimeter(self):

        return (self._perimeter)

from src.Figure import Figure


class Rectangle(Figure):
    __side_a = 0
    __side_b = 0

    def __init__(self, side_a, side_b):
        if side_a > 0 and side_b > 0:
            self.name = "Rectangle"
            self.__side_a = side_a
            self.__side_b = side_b
            self._area = self.__side_a * self.__side_b
            self._perimeter = 2 * (self.__side_a + self.__side_b)
        else:
            raise Exception("SIDE LESS THEN ZERO")

    @property
    def area(self):
        return (self._area)

    @property
    def perimeter(self):
        return (self._perimeter)

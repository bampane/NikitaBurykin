from src import Figure

class Square(Figure):
    _side=0
    def __init__(self,side):
        self.name=Square
        self.side=side
    @property
    def area(self):
        return (self.side*self.side)


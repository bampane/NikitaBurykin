class Figure:

    def __init__(self):
        self._area = 0
        self._perimeter = 0
        self._name = ""

    def add_area(self, fig):
        if isinstance(fig, Figure):
            return self.area + fig.area
        else:
            raise ValueError("TRY ADD WRONG CLASS")

class Cell:

    def __init__(self, number):
        self._number = number

    def __add__(self, other):
        return Cell(self._number + other._number)

    def __sub__(self, other):
        if (self.number - other.number) > 0:
            return self._number - other._number

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return self.number / self.other


a = Cell(2)
print(a.__add__())

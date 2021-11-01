# class Warehouse:

class Equipment:

    def __init__(self, name, price, amount, guarantee):
        self.name = name
        self.price = price
        self.amount = amount
        self.guarantee = guarantee
        # self.my_list = []


class Printer(Equipment):
    def __init__(self, *args):
        super().__init__(*args)
        print(f'{self.name} {self.price} {self.amount} {self.guarantee}')


class Copy(Equipment):
    def __init__(self, *args):
        super().__init__(*args)
        print(f'{self.name} {self.price} {self.amount} {self.guarantee}')


class Xerox(Equipment):
    def __init__(self, *args):
        super().__init__(self, *args)
        print(f'{self.name} {self.price} {self.amount} {self.guarantee}')


# a = Printer('PEp', 230, 20, 23)
# print(a)
b = Xerox('Ziko', 345, 10, 120)
print(b)

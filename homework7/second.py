from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self,number):
        self.number = number

    @abstractmethod
    def result(self):
        pass

    def __add__(self, other):
        return self.number + other.number

class Suite(Clothes):

    def result(self):
        return 2* self.number + 0.3

class Coat(Clothes):

    def result(self):
        return self.number/6.5 + 0.5



a = Suite(30)

b = Coat(200)

print(a.result())
print(b.result())


print(a + b)
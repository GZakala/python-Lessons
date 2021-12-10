from abc import ABC, abstractmethod



class Cloth(ABC):

    count = 0


    def __init__(self, name):
        self.name = name

    
    @abstractmethod
    def expenses(value):
        pass



class Suit(Cloth):

    def __init__(self, H: float):
        super().__init__(self)
        self.H = H

    @property
    def expenses(self):
        a = round(2 * self.H + 0.3, 1)
        Cloth.count += a
        return a



class Coat(Cloth):

    def __init__(self, V: float):
        super().__init__(self)
        self.V = V


    @property
    def expenses(self):
        a = round(self.V / 6.5 + 0.5, 1)
        Cloth.count += a
        return a


a = Suit(34)
b = Coat(44)
print(a.expenses)
print(b.expenses)
print(a.count)


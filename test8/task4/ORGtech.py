class ORGtech:

    def __init__(self, name: str, inv_number: int, brand: str, model: str):
        self.name = name
        self.inv_number = inv_number
        self.brand = brand
        self.model = model


    def __repr__(self):
        return f'Base class for org technic.\nName: {self.name}\nInv_number: {self.inv_number}'



class PC(ORGtech):

    def __init__(self, name: str, inv_number: int, brand: str, model: str, monoblock = True):
        super().__init__(name, inv_number, brand, model)
        self.monoblock = monoblock


    def __repr__(self):
        if self.monoblock is True:
            a = 'yes'
        else:
            a = 'no'
        return f'PC\nName: {self.name}, Inv_number {self.inv_number}\nBrand: {self.brand}, Model: {self.model}, is Monoblock: {a}'



class Printer(ORGtech):

    def __init__(self, name: str, inv_number: int, brand: str, model: str, color = True):
        super().__init__(name, inv_number, brand, model)
        self.color = color


    def __repr__(self):
        if self.color is True:
            a = 'yes'
        else:
            a = 'no'
        return f'Printer\nName: {self.name}, Inv_number {self.inv_number}\nBrand: {self.brand}, Model: {self.model}, is color: {a}'



class Scaner(ORGtech):

    def __init__(self, name: str, inv_number: int, brand: str, model: str, in_printer = True):
        super().__init__(name, inv_number, brand, model)
        self.in_printer = in_priter


    def __repr__(self):
        if self.in_printer is True:
            a = 'yes'
        else:
            a = 'no'
        return f'Scaner\nName: {self.name}, Inv_number {self.inv_number}\nBrand: {self.brand}, Model: {self.model}, In printer: {a}'



class Xerox(ORGtech):

    def __init__(self, name: str, inv_number: int, brand: str, model: str, in_printer = True):
        super().__init__(name, inv_number, brand, model)
        self.in_printer = in_printer


    def __repr__(self):
        if self.in_printer is True:
            a = 'yes'
        else:
            a = 'no'
        return f'Xerox\nName: {self.name}, Inv_number {self.inv_number}\nBrand: {self.brand}, Model: {self.model}, In printer: {a}'



class Shredder(ORGtech):

    def __repr__(self):
        return f'Shredder\nName: {self.name}, Inv_number {self.inv_number}\nBrand: {self.brand}, Model: {self.model}'


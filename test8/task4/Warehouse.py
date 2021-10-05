class Warehouse:

    all_invent = 0
    all_accounting = {}

    def __init__(self, name, specification, comment):
        if name is not str or specification is not str or comment is not str:
            print('The values must be string type')
            return
        else:
            self.name = name
            self.specification = specification
            self.comment = comment
        self.__class__.all_invent += 1
        self.__class__.all_accounting[self.__class__.all_invent] = (self.name, self.specification, self.comment)


    def __repr__(self):
        return f'Base class for warehouse'



class PC_shelf(Warehouse):

    invent = 1000
    accounting = {}
    
    def __init__(self, name, specification, comment):
        super().__init__(name, specification, comment)
        self.__class__.invent += 1
        self.__class__.accounting[self.__class__.invent] = (self.name, self.specification, self.comment)


    def __repr__(self):
        return f'Invent number: {self.__class__.invent}\n{self.__class__.accounting[self.__class__.invent]}'




class Printer_shelf(Warehouse):

    invent = 0
    accounting = {}

    def __init__(self, name, specification, comment):
        super().__init__(name, specification, comment)
        self.invent += 1
        self.__class__.accounting[self.__class__.invent] = (self.name, self.specification, self.comment)


    def __repr__(self):
        return f'Invent number: {self.__class__.invent}\n{self.__class__.accounting[self.__class__.invent]}'
    


class Scaner_shelf(Warehouse):

    invent = 5000
    accounting = {}

    def __init__(self, name, specification, comment):
        super().__init__(name, specification, comment)
        self.invent += 1
        self.__class__.accounting[self.__class__.invent] = (self.name, self.specification, self.comment)


    def __repr__(self):
        return f'Invent number: {self.__class__.invent}\n{self.__class__.accounting[self.__class__.invent]}'
    


class Xerox_shelf(Warehouse):
    
    invent = 6000
    accounting = {}

    def __init__(self, name, specification, comment):
        super().__init__(name, specification, comment)
        self.invent += 1
        self.__class__.accounting[self.__class__.invent] = (self.name, self.specification, self.comment)


    def __repr__(self):
        return f'Invent number: {self.__class__.invent}\n{self.__class__.accounting[self.__class__.invent]}'
    


class Shredder_shelf(Warehouse):
    
    invent = 8000
    accounting = {}

    def __init__(self, name, specification, comment):
        super().__init__(name, specification, comment)
        self.invent += 1
        self.__class__.accounting[self.__class__.invent] = (self.name, self.specification, self.comment)


    def __repr__(self):
        return f'Invent number: {self.__class__.invent}\n{self.__class__.accounting[self.__class__.invent]}'
    


a = Shredder_shelf('shredder', 'blablabla', 'mkdmcdncjd')
print(a)

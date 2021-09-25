class Stationery:

    def __init__(self, title: str):
        self.__title = title


    def get_title(self):
        return self.__title


    def draw(self):
        return 'Starting rendering'



class Pen(Stationery):

    def draw(self):
        return f'We write with a {Stationery.get_title(self)} in a book'



class Pencil(Stationery):

    def draw(self):
        return f'We make a drawing with a {Stationery.get_title(self)}'



class Handle(Stationery):

    def draw(self):
        return f'We circle the text with a {Stationery.get_title(self)}'



pen = Pen(title='pen')
print(pen.draw())
print()

pencil = Pencil(title='pencil')
print(pencil.draw())
print()

handle = Handle(title='handle')
print(handle.draw())


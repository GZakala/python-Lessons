class Cell:

    def __init__(self, cell_count):
        self.cell_count = cell_count


    def __add__(self, other):
        result = self.cell_count + other.cell_count
        return Cell(result)


    def __sub__(self, other):
        if self.cell_count <= other.cell_count:
            print('результат не может быть 0 или меньше 0')
        else:
            result = self.cell_count - other.cell_count
            return Cell(result)


    def __mul__(self, other):
        result = self.cell_count * other.cell_count
        return Cell(result)


    def __truediv__(self, other):
        result = self.cell_count // other.cell_count
        return Cell(result)


    def __str__(self):
        return f'{"*" * self.cell_count}'


    def make_order(self, count_on_line=5):
        result = []
        for i in range(self.cell_count // count_on_line):
            result.append(f'{"*" * count_on_line}')

        if self.cell_count % count_on_line != 0:
            result.append(f'{"*" * (self.cell_count % count_on_line)}')
        return '\n'.join(result)



a = Cell(7)
b = Cell(3)
 
print(a + b)
print()
print(a - b)
print()
print(a * b)
print()
print(a / b)
print()
print(a.make_order(3))


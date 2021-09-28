class Matrix:

    def __init__(self, value):
        self.value = value


    def __str__(self):
        result = []
        for line in self.value:
            app = [str(i) for i in line]
            result.append('  '.join(app))

        result = '\n'.join(result)
        return result


    def __add__(self, other):
        result = []
        for num_line, line in enumerate(self.value):
            result_el = []
            for num_el, el in enumerate(line):
                i = el + other.value[num_line][num_el]
                result_el.append(i)
            result.append(result_el)
        return Matrix(result)
                
                


a = Matrix([[2, 4, 5], [3, 2, 1]])
print(a)

b = Matrix([[3, 3, 3], [2, 2, 2]])
print()
print(b)

print()
print(a + b)


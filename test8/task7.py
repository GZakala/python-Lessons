import math



class ComplexNumbers:

    def __init__(self, *args):
        self.a = list(args)


    def __repr__(self):
        return f'Class of complex numbers\nResult = {self.a}'


    def y__add__(self, other):
        len_s = len(self.a)
        len_o = len(other.a)
        if len_s > len_o:
            const = len_s - len_o
            while const > 0:
                other.a.append(0)
                const -= 1
        elif len_s < len_o:
            const = len_o - len_s
            while const > 0:
                self.a.append(0)
                const -= 1
        result = [el + other.a[i] for i, el in enumerate(self.a)]
        return ComplexNumbers(*result) 


    def __sub__(self, other):
        len_s = len(self.a)
        len_o = len(other.a)
        if len_s > len_o:
            const = len_s - len_o
            while const > 0:
                other.a.append(0)
                const -= 1
        elif len_s < len_o:
            const = len_o - len_s
            while const > 0:
                self.a.append(0)
                const -= 1
        result = [el - other.a[i] for i, el in enumerate(self.a)]
        return ComplexNumbers(*result) 


    def __mul__(self, other):
        len_s = len(self.a)
        len_o = len(other.a)
        if len_s > len_o:
            const = len_s - len_o
            while const > 0:
                other.a.append(1)
                const -= 1
        elif len_s < len_o:
            const = len_o - len_s
            while const > 0:
                self.a.append(1)
                const -= 1
        result = [el * other.a[i] for i, el in enumerate(self.a)]
        return ComplexNumbers(*result) 


    def __truediv__(self, other):
        len_s = len(self.a)
        len_o = len(other.a)
        if len_s > len_o:
            const = len_s - len_o
            while const > 0:
                other.a.append(1)
                const -= 1
        elif len_s < len_o:
            const = len_o - len_s
            sub = len_s
            while const > 0:
                self.a.append(other.a[sub] ** 2)
                const -= 1
                sub += 1
        result = [el / other.a[i] for i, el in enumerate(self.a)]
        return ComplexNumbers(*result) 


    def __floordiv__(self, other):
        len_s = len(self.a)
        len_o = len(other.a)
        if len_s > len_o:
            const = len_s - len_o
            while const > 0:
                other.a.append(1)
                const -= 1
        elif len_s < len_o:
            const = len_o - len_s
            sub = len_s
            while const > 0:
                self.a.append(other.a[sub] ** 2)
                const -= 1
                sub += 1
        result = [el // other.a[i] for i, el in enumerate(self.a)]
        return ComplexNumbers(*result) 


    def __mod__(self, other):
        len_s = len(self.a)
        len_o = len(other.a)
        if len_s < len_o:
            const = len_o - len_s
            res = []
            for _ in range(const):
                res.append(other.a[-1])
                del(other.a[-1])
            result = [el % other.a[i] for i, el in enumerate(self.a)]
            for _ in range(const):
                result.append(res[-1])
                del(res[-1])
        elif len_s > len_o:
            const = len_s - len_o
            res = []
            for _ in range(const):
                res.append(self.a[-1])
                del(self.a[-1])
            result = [el % other.a[i] for i, el in enumerate(self.a)]
            for _ in range(const):
                result.append(res[-1])
                del(res[-1])    
        else:
            result = [el % other.a[i] for i, el in enumerate(self.a)]
        return ComplexNumbers(*result)  


    def __pow__(self, other):
        len_s = len(self.a)
        len_o = len(other.a)
        if len_s < len_o:
            const = len_o - len_s
            res = []
            for _ in range(const):
                res.append(other.a[-1])
                del(other.a[-1])
            result = [el % other.a[i] for i, el in enumerate(self.a)]
            for _ in range(const):
                result.append(res[-1])
                del(res[-1])
        elif len_s > len_o:
            const = len_s - len_o
            res = []
            for _ in range(const):
                res.append(self.a[-1])
                del(self.a[-1])
            result = [el % other.a[i] for i, el in enumerate(self.a)]
            for _ in range(const):
                result.append(res[-1])
                del(res[-1])    
        else:
            result = [el ** other.a[i] for i, el in enumerate(self.a)]
        return ComplexNumbers(*result)


a = ComplexNumbers(38, 88, 3)
b = ComplexNumbers(13, 1, 9)
print(a ** b)

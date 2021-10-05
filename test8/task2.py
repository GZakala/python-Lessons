class ZeroDivError(ZeroDivisionError):

    def __init__(self):
        self.txt = f'Divisior by 0 is prohibited!'



def div(a, b):
    while b == 0:
        print(ZeroDivError())
        b = int(input('Enter new divisior: '))
    return a / b
        


print(div(3, 0))


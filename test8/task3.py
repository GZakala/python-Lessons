class OnliNumberError(ValueError):

    def __init__(self, txt):
        self.txt = txt


    def __repr__(self):
        return f'Это значения не является значением типа "int": {self.txt}'



result = []
while True:
    nn = input('Add new number: ')
    if nn == 'stop':
        result = [int(nn) for nn in result]
        print(result)
        break
    
    try:
        int(nn)
    except ValueError:
        print(repr(OnliNumberError(nn)))
        continue

    result.append(nn)


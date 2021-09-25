class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width


    def mass(self, kg, sm):
        return f'{round(self.__length * self.__width * kg * sm) / 1000} tonn'


MKAD = Road(5000, 20)
print(MKAD.mass(25, 5))


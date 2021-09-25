class Worker:

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.__name = name
        self.__surname = surname
        self.__position = position
        self.__wage = wage
        self.__bonus = bonus

    
    def get_name(self):
        return self.__name


    def get_surname(self):
        return self.__surname


    def get_position(self):
        return self.__position


    def get_wage(self):
        return self.__wage


    def get_bonus(self):
        return self.__bonus



class Position(Worker):

    def get_full_name(self):
        return f'{Worker.get_name(self)} {Worker.get_surname(self)}'


    def get_total_income(self):
        return {'wage': Worker.get_wage(self), 'bonus': Worker.get_bonus(self)}



Mike = Position(name='Mike', surname='Vasovski', position='Support manager', wage='40000', bonus='5000')
print(Mike.get_full_name())
print(Mike.get_total_income())


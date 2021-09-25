class Car:

    def __init__(self, speed: int, color: str, name: str, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police


    def go(self):
        print(f'{self.name} is going')


    def stop(self):
        print(f'{self.name} spped')


    def turn(self, side):
        print(f'{self.name} turned on {side}')


    def show_speed(self):
        print(f'Speed: {self.speed}')



class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Speeding!!!: {self.speed}')
        else:
            print(f'Speed: {self.speed}')



class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Speeding!!!: {self.speed}')
        else:
            print(f'Speed: {self.speed}')



class SportCar(Car):

    def boost(self, nitro: bool):
        if nitro is True:
            print(self.speed + 30)
        else:
            print(self.speed)



class PoliceCar(Car):

    def signal(self, signal: bool):
        if signal is True:
            print('Signal on')
        else:
            print('Signal off')



mers = TownCar(name='mers', color='white', speed=65)
mers.go()
mers.show_speed()

logan = WorkCar(name='logan', color='brown', speed=46)
print()
logan.go()
logan.show_speed()
logan.stop()

BMW = SportCar(name='BMW', color='blue', speed=110)
print()
BMW.go()
BMW.turn('right')
BMW.show_speed()
BMW.boost(True)

lada = PoliceCar(name='lada', color='black', speed=23)
print()
lada.go()
lada.signal(True)
lada.turn('right')
lada.show_speed()


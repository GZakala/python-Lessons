import time
import itertools



class TrafficLight:

    def __init__(self, color: str):
        self.__color = color
        self.__colors = ['red', 'yellow', 'green']
        self.__time = [7, 2,5]


    def running(self):
        while True:
            if self.__color not in self.__colors[0]:
                self.__colors.insert(0, self.__colors[-1])
                del self.__colors[-1]
                self.__time.insert(0, self.__time[-1])
                del self.__time[-1]
            else:
                break

        for i in itertools.cycle(self.__colors):
            print(i)
            time.sleep(self.__time[self.__colors.index(i)])


reds = TrafficLight('yellow')
print(reds.running())


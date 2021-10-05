import datetime
import math


class Date:

    def __init__(self, date):
        self.date = date


    @classmethod
    def int_date(cls, date):
        result = date.split('-')
        result = [int(n) for n in result]
        return result


    @staticmethod
    def valid_date(date):
        try:
            date = [int(n) for n in date.split('-')]
        except ValueError:
            return f'Некорректный ввод данных'

        if date[1] < 1 or date[1] > 12:
            return f'В году ровно 12 месяцев\nВы написали {date[2]}'
        
        m = date[1]
        y = date[2]
        # Две нижние формулы находят максимальное количество дней
        # в любом месяце, учитывая високосные года
        # Формула была взята на хабре
        const = (1 - math.floor((y % 4 + 2) / (y % 4 + 1))) * math.floor((y % 100 + 2) / (y % 100 + 1)) + (1 - math.floor((y % 400 + 2) / (y % 400 + 1)))
        max_day = 28 + (m + (m // 8)) % 2 + 2 % m + (1 + const) // m + 1 // m - const // m
        
        if date[0] > max_day:
            if max_day == 31:
                was = 'был'
                days = 'день'
            else:
                was = 'было'
                days = 'дней'
            return f'В {date[1]} месяце {date[2]} года {was} {max_day} {days}\nВы написали {date[0]}'
        elif date[0] < 1:
            return f'В месяце не может быть меньше 1 дня\nВы написали {date[0]}'
        else:
            return f'Валидация прошла успешно'



a = Date.valid_date('30-02-1939')
print(a)


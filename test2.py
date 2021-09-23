# task 1
type_list = ['str', 12, True]
for x in type_list:
    print(type(x))


# 2 task
x = int(input('How many numbers you want to add: '))
shuffle_list = []
y = x

while x > 0:
    shuffle_list.append(int(input('Write your number: ')))
    x -= 1

i = 0
while i + 1 < y:
    shuffle_list[i], shuffle_list[i + 1] = shuffle_list[i + 1], shuffle_list[i]
    i += 1

print(shuffle_list)


# 3 task
year_time_l = [('January', 'February', 'December'), ('Mart', 'Aprel', 'May'), ('June', 'Jule', 'August'), ('September', 'Octomber', 'November')]
year_time_d = {
    'Winter': ('December', 'January', 'February'),
    'Spring': ('Mart', 'Aprel', 'May'),
    'Summer': ('June', 'Jule', 'August'),
    'Autumn': ('September', 'Octomber', 'November')
}

month = input('Enter the month: ')

if month in year_time_l[0]:
    print('Winter')
elif month in year_time_l[1]:
    print('Spring')
elif month in year_time_l[2]:
    print('Summer')
elif month in year_time_l[3]:
    print('Autumn')


for x in year_time_d:
    if month in year_time_d[x]:
        print(x)


# 4 task
text = input()
text = text.split()

i = 1
for line in text:
    if len(line) > 10:
        print(f'{i}: {line[0:10]}')
    else:
        print(f'{i}: {line}')
    i += 1


# 5 task
my_list = [7, 5, 3, 3, 2]
n = int(input())

if n >= my_list[-1]:   
    for a in my_list:
        x = my_list.index(a) 
        if n >= a:
            if x == 0:
                my_list = [n] + my_list
                break
            elif x != 0:
                my_list = my_list[:x] + [n] + my_list[x:]
                break
            else:
                continue
else:
    my_list = my_list + [n]

print(my_list)


# 6 task
num_of_product = int(input('Write, haw many products you want to add: '))
table_product = []
i = 1

name_list = []
price_list = []
quanity_list = []
units_list = []

for product in range(num_of_product):
    name = str(input('Name of your product: '))
    price = int(input('Your product price: '))
    quanity = int(input('How many units of production: '))
    units = str(input('Units of measurement: '))

    name_list.append(name)
    price_list.append(price)
    quanity_list.append(quanity)
    units_list.append(units)

    dict_product = {
        "name": name,
        "price": price,
        "quanity": quanity,
        "units": units,
    }

    tuple_product = (i, dict_product)
    
    table_product.append(tuple_product)

    i += 1

print(table_product)

statistics_dict = {
    'name': name_list,
    'price': price_list,
    'quanity': quanity_list,
    'units': units_list,
}

print(statistics_dict)
# task 1
def div(a, b):
    if b == 0:
        print('Деление на ноль невозможно')
        return
    return a / b


if __name__ == '__main__':
    print(div(8, 2))


# task 2
def person(**kwargs):
    return f' Name: {kwargs["name"]} \n Last name: {kwargs["lastName"]} \n Date of birth: {kwargs["dateOfBirth"]} \n Cyty: {kwargs["city"]} \n Email: {kwargs["email"]} \n Number: {kwargs["number"]}'


if __name__ == '__main__':
    print(person(name = 'George', lastName = 'Zakala', dateOfBirth = '14.06.2000', city = 'Moscow', email = 'fenedgaik@mail.ru', number = 89268879646))


# task 3
def my_func(a, b, c):
    return a + b + c - min(a, b, c)

if __name__ == '__main__':
    print(my_func(6, 8, 10))


# task 4
def degree(x, y):
    const = abs(y)
    n = x
    while const > 1:
        x *= n
        const -= 1

    return 1 / x


if __name__ == '__main__':
    print(degree(2, -3))


# task 5
def summ():
    flag = False
    result = 0
    while True:
        x = str(input())
        x = x.split()
        for item in x:
            if item == 'exit':
                flag = True
            else:
                result = result + int(item)
        
        print(result)
        if flag == True:
            break
    return 'The End'


if __name__ == '__main__':
    print(summ())


# task 6
def int_func(string: str):
    return string.title()


if __name__ == '__main__':
    print(int_func('nice day'))

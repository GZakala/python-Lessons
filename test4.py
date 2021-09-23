import random
import itertools
import functools


# task 1
def salary(hour, payment, prize):
    return f'Salary = {hour * payment + prize}'

print(salary(30, 500, 2000))



# task 2
numbers = [random.randint(0, 300) for i in range(10)]
print([i for i in numbers[1:] if i > numbers[numbers.index(i) - 1]])



# task 3
print([i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0])



# task 4
numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
for i in numbers[:]:
    if numbers.count(i) == 1:
        result.append(i)

print(result)



# task 5
numbers = [i for i in range(100, 1001) if i % 2 == 0]
print(functools.reduce(lambda x, y: x + y, numbers))



# task 6
for i in itertools.count(10):
    print(i, end=' ')
    if i > 18:
        print()
        break

numbers = [2, 4, 5]
for i, j in enumerate(itertools.cycle(numbers)):
    print(j, end=' ')
    if i > 18:
        print()
        break



# task 7
def fact(num):
    const = 1
    numbers = []
    for i in range(num):
        const *= i + 1
        numbers.append(f'{i + 1} *')
    numbers[-1] = f'{i + 1}'
    summer = ' '.join(numbers)
    return f'!{num} = {summer} = {const}'


print(fact(10))

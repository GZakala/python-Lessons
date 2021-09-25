import random
import json
import functools



# task 1
with open('task1.txt', 'w', encoding='utf-8') as f:
    while True:
        text = input()
        if text != '':
            f.writelines(f'{text}\n')
        else:
            print()
            break



# task 2
with open('task2.txt', 'r', encoding='utf-8') as f:
    content = []
    const = 0
    for i in f.readlines():
        content.append(i.split())
        print(f'In {const + 1} line - {len(content[const])} words')
        const += 1
    print()
    print(f'Total of {len(content)} lines')



# task 3
with open('task3.txt', 'r', encoding='utf-8') as f:
    workers = []
    for i in f.readlines():
        surname, salary = i.split()
        workers.append((surname, salary))
    
    for i in workers:
        print(i[0])

    for i in workers:
        if int(i[1]) < 20000:
            print()
            print(f'{i[0]} has salary less than 20000')



# task 4
with open('task4.txt', 'r', encoding='utf-8') as f:
    content = []
    const = 0
    for i in f.readlines():
        content.append(i.split())
        if const == 0:
            content[const][0] = 'Один'
        elif const == 1:
            content[const][0] = 'Два'
        elif const == 2:
            content[const][0] = 'Три'
        elif const == 3:
            content[const][0] = 'Четыре'
        const += 1

with open('task4+.txt', 'w', encoding='utf-8') as f:
    for i in content:
        f.write(f"{' '.join(i)} \n")



# task 5
with open('task5.txt', 'w', encoding='utf-8') as f:
    f.write(''.join([f'{random.randint(0, 100)} ' for i in range(10)]))

with open('task5.txt', 'r', encoding='utf-8') as f:
    result = [i for i in f.read().split(' ')]
    del(result[-1])

print(functools.reduce(lambda x, y: int(x) + int(y), result))



# task 6
with open('task6.txt', 'r', encoding='utf-8') as f:
    result = {}
    for line in f.readlines():
        i = line.split() 
        lesson = i[0]
        del(i[0])
        numbers = [''.join(n for n in s if n.isdigit()) for s in i]
        for i in numbers:
            if i == '':
                numbers.remove(i)
        result[lesson] = functools.reduce(lambda x, y: int(x) + int(y), numbers)
    print(result)



# task 7
with open('task7.txt', 'r', encoding='utf-8') as f:
    result = []
    firms = {}
    avarage_profit = {}
    avarage = []
    for line in f.readlines():
        line = line.split()
        firms[line[0]] = int(line[2]) - int(line[3])
        avarage.append(int(line[2]))    

    avarage_profit['avarage_profit'] = sum(avarage) / len(avarage)
    result.append(firms)
    result.append(avarage_profit)

print(result)

with open('task7.json', 'w') as f:
    json.dump(result, f)

# 1 task
a = 4
b = 2

a, b = int(input('number a: ')), int(input('number b: '))

print(a, b, sep=' and ')
print()

# 2 task
time = int(input('Write time in the second: '))

hh = time // (60 * 60)
mm = (time - hh * 60 * 60) // 60
ss = time % 60

print(f'{hh}:{mm}:{ss}')
print()

# 3 task
n = int(input('Write n number: '))

nn = int(str(n) + str(n))
nnn = int(str(nn) + str(n))

print(n + nn + nnn)
print()

# 4 task
x = input('Write number whues max number you want to know: ')

x = list(str(x))
result = [int(item) for item in x]

print(max(result))
print()

# 5 task
revenue = int(input('Write revenue your firm: '))
costs = int(input('Write your firm costs: '))

if revenue > costs:
    print('Your company is profitable!')
    print('Return of revenue: ', revenue / costs, sep='')
    worker_count = int(input('Write count of worker in your firm: '))
    print('Firm revenue on one worker - ', revenue / worker_count)
elif costs > revenue:
    print('Your company is unprofitable.')

print()

# 6 task
result_in_first_day = int(input('Write result in first day: '))
result_in_last_day = int(input('Write result in last day: '))

i = 1
while result_in_first_day < result_in_last_day:
    result_in_first_day = result_in_first_day + (result_in_first_day / 10)
    i += 1


print('Atlete run the distanse on day ', i, sep='')
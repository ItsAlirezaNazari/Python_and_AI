import random

n = int(input('Enter a num: '))
list = []

for i in range(n):
    while True:
        r = random.randint(1, n + 100)
        
        if r not in list:
            list.append(r)
            break

print(list)

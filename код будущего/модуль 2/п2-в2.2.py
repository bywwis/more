import random
n, k = int(input('n = ')), int(input('k = '))
a = [random.randint(1, 100) for el in range(n)]

print('Исходный список: ', *a)

queue = []
for i in range(n-k+1):
    queue.append(min(a[i:i+k]))

print('Результат: ')
while len(queue) != 0: #можно просто queue
    print(queue.pop(0), end=' ')


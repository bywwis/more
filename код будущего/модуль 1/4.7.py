a = [int(el) for el in input().split()]

count = 0
n = len(a)

for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % 13 == 0 and (a[i] % 2 != 0 or a[j] % 2 != 0):
            count += 1

if count != 0:
    print('Пар = ', count)
else:
    print('Таких пар нет')




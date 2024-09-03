a = [int(el) for el in input().split()]

n = len(a)
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % 37 == 0:
            count += 1
if count:
    print('Пар = ', count)
else:
    print('Таких пар нет')
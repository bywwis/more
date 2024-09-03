a = [int(el) for el in input().split()]

count = 0

for i in range (len(a) - 1):
    if (a[i] + a[i + 1]) % 3 == 0 and (a[i] + a[i + 1]) % 9 != 0:
        count += 1

if count != 0:
    print('Количество пар элементов = ', count)
else:
    print('Таких пар нет')

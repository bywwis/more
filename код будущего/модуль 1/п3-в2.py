s = set()
for i in range(10):
    a = input('Введите слово: ')
    s.add(a)

for index, a in enumerate(s):
    print('Это {} из элементов множества: {}'.format('один' if index == 0 else 'ещё один', a))



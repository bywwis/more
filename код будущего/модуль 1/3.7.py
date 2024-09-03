numbers = [2, 5, 5, 6, 3]
num = None
for i in range(len(numbers)):
    if numbers[i] < 0:
        num = i
        break

if num is None:
    print('отрицательных нет')
else:
    print(num)
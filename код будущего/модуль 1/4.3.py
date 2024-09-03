numbers = [1, 2, 4, 3, 4, 28, 4, 5, 6, 8, 10, 5, 9, 10, 8, 56]

n = len(numbers)
min_el = 9999999999999999999999

for i in range(n):
    for j in range(n):
        if (i != j and
                (min_el > numbers[i] * numbers[j] and
                 numbers[i] * numbers[j] % 14 == 0 and
                 (numbers[i] % 2 == 0 or numbers[j] % 2 == 0))):
            min_el = numbers[i] * numbers[j]


print(min_el)
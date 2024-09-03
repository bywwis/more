numbers = [1, 2, 3, 4, 5, 6,  50, 25, 400]
res = max(numbers, key=lambda x: x % 25)
print(res)

#наибольший остаток от деления на 25
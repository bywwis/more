num = int(input())

#sum = 0
#n = num

#while n > 0:
 #   sum += n % 10
  #  n = n // 10

s1 = sum([int(el) for el in str(num)])
if num % s1 == 0:
    print('Это число харшад')
else:
    print('Обычное число')
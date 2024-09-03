n = int(input())
a = 1
b = 1
for i in range(n-2):
    next_num = a + b
    a = b
    b = next_num
    print(b, end=' ')

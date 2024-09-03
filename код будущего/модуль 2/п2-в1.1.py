n, m = int(input()), int(input())
A = []
count = 1
for i in range(n):
    row = []
    for j in range(m):
        row.append(count)
        count += 1
    if i % 2 != 0:
        row.reverse()
    A.append(row)
print('Matrix result:')
for row in A:
    print(*row, sep='\t')

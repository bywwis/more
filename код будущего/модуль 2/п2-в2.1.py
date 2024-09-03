n, m = int(input()), int(input())
A = []
count = 1
for i in range(m):
    row = []
    for j in range(n):
        row.append(count)
        count += 1
    row.reverse()
    A.append(row)

AT = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(A[j][i])
    AT.append(row)
print('Matrix result:')
for row in AT:
    print(*row, sep='\t')

import random
print('Введите размеры матрицы')
n, m = int(input('n = ')), int(input('m = '))
A = []
for _ in range(n):
    row = []
    for _ in range(m):
        row.append(random.randint(0, 2))
    A.append(row)

print('Исходная матрица: ')
for row in A:
    print(*row, sep='\t')

x, y = int(input('Введите номер строки заливки (нумерация начинается с 0): ')), int(input('Введите номер столбца заливки (нумерация начинается с 0): '))
f = int(input('Введите новый цвет заливки: '))

queue = [(x, y)]
visited = [[False for _ in range(m)] for _ in range(n)]
x_f, y_f = x, y
f_0 = A[x][y]

while queue:
    pixel = queue.pop(0)
    x, y = pixel
    if visited[x][y]:
        continue
        visited[x][y] = True

    if A[x][y] == f_0:
        A[x][y] = f

    if x > 0 and A[x - 1][y] == f_0:
        queue.append((x - 1, y))
    if y > 0 and A[x][y - 1] == f_0:
        queue.append((x, y - 1))
    if x < n - 1 and A[x + 1][y] == f_0:
        queue.append((x + 1, y))
    if y < m - 1 and A[x][y + 1] == f_0:
        queue.append((x, y + 1))

print('Матрица после заливки')
for row in A:
    print(*row, sep='\t')

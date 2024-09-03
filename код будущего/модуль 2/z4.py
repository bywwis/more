import random

# Ввод размеров списка
n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

# Создание двумерного списка со случайными значениями
matrix = [[random.randint(0, 2) for _ in range(m)] for _ in range(n)]

# Вывод первоначального списка
print("Первоначальный список:")
for row in matrix:
    print(row)

# Ввод координат точки заливки и цвета заливки
x = int(input("Введите номер строки точки заливки: "))
y = int(input("Введите номер столбца точки заливки: "))
color = int(input("Введите цвет заливки: "))


# Функция для заливки области заданным цветом
def flood_fill(matrix, x, y, color):
    rows = len(matrix)
    cols = len(matrix[0])

    def fill(matrix, x, y, prev_color, new_color):
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return
        if matrix[x][y] != prev_color:
            return

        matrix[x][y] = new_color

        fill(matrix, x - 1, y, prev_color, new_color)
        fill(matrix, x + 1, y, prev_color, new_color)
        fill(matrix, x, y - 1, prev_color, new_color)
        fill(matrix, x, y + 1, prev_color, new_color)

    prev_color = matrix[x][y]
    fill(matrix, x, y, prev_color, color)


# Заливка области заданным цветом
flood_fill(matrix, x, y, color)

# Вывод списка после заливки
print("Список после заливки:")
for row in matrix:
    print(row)

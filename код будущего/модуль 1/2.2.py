a = float(input())
b = float(input())
c = float(input())

D = b**2 - 4 * a * c

match  D >= 0:
    case False:
        print('нет решений')
    case True:
        x1 = (-b + D**(0.5)) / (2 * a)
        x2 = (-b - D**(0.5)) / (2 * a)
        print(x1, x2)
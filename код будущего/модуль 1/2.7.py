def squard(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b - D ** (0.5))/(2*a)
        x2 = (-b + D ** (0.5))/(2*a)
        return [x1, x2]
    elif D == 0:
        return -b /(2*a)
    else:
        return None

print(squard(1, 2, 1)) #1 koren
print(squard(1, 3, -4)) #2 kornya
print(squard(1, 1, 1)) #korney net

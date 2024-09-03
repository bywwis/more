a = list(range(-1000, 1001))
n = len(a)
min_el = max(a) ** 2
pare = ()
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] * a[j]) % 33 == 0 and min_el > a[i] * a[j]:
            min_el = a[i] * a[j]
            pare = (a[i], a[j])
print(pare)



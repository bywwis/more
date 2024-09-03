a = [1, 2, 3, 4, 5, 6]

S = sum(a)
count = a.count(max(a))
a.append(S)
a.append(count)

print(a)
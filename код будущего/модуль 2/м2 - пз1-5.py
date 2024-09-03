abc = ''.join([chr(el) for el in range(ord('А'), ord('я')+1)])
print(abc)
s = input()
sp = []
for el in s:
    if el in abc:
        sp.append(el)
print(sp)
# Без использования индексации
s = input()
s_new = ''.join([el*2 for el in s if el != ' '])
print(s_new)

# С использованием индексации
s = input()
n = len(s)
s_new = ''
for i in range(n):
    if s[i] != " ":
        s_new += s[i] * 2
    else:
        s_new += s[i]

print(s_new)


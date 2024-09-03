# С использованием индексации
s = input()
s_new = ''
for i in range(len(s)):
    if not s[i].isdigit():
        s_new += s[i]
print(s_new)

# Без использования индексации
s = input()
s_new = ''.join([el for el in s if not el.isdigit()])
print(s_new)

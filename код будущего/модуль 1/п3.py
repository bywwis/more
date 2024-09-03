n = int(input())
m = int(input())

set1 = set(range(n, m+1))
set2 = set()

for num in set1:
    if '7' in str(num):
        set2.add(num)

for num in set2:
    print(num)

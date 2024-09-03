A = [81, 226, 57, 32, 112, 56, 0]

n = len(A)
for i in range(n):
    for j in range(i + 1, n):
        if (A[i] + A[j]) % 113 == 0:
            print((A[i], A[j]))

import timeit
def optim_eratosthenes(n):
    m = (n - 1) // 2
    a = [True] * (m + 1)
    i = 0
    while i * i < n // 2:
        if a[i]:
            num = i * 2 + 3
            a[i + num:m:num] = [False] * ((m - i - num - 1) // num + 1)
        i += 1
    return [2] + [i * 2 + 3 for i in range(m) if a[i]]

if __name__ == '__main__':
    n = int(input())
    start_time = timeit.default_timer()
    result = optim_eratosthenes(n)
    end_time = timeit.default_timer()

    print('Простые числа')
    print(*result)
    print(f'Вычисление (оптимизированное решето Эратосфена) заняло {end_time - start_time} секунд')

#Решето Сундарама
import timeit
def sundaram(n):
    k = (n - 2) // 2
    a = [True] * (k + 1)
    for i in range(1, k + 1):
        j = i
        while i + j + 2 * i * j <= k:
            a[i + j + 2 * i * j] = False
            j += 1
    return a

if __name__ == '__main__':
    n = int(input())
    start_time = timeit.default_timer()
    result = sundaram(n)
    end_time = timeit.default_timer()
    print('Простые числа')
    print(2, end=' ')
    print(*[2*el + 1 for el in range(1, len(result)) if result[el]])
    print(f'Вычисление (решето Сундарама) заняло {end_time - start_time} секунд')




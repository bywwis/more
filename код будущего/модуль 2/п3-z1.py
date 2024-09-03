#решето эратосфена
import timeit
def prostoe(number):
    flag = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            flag = False
            break
    return flag

def eratosthenes(n):
    a = [True] * (n + 1)
    k = 2
    while k * k <= n:
        if a[k]:
            i = k * k
            while i <= n:
                a[i] = False
                i += k
        k += 1
    return a


if __name__ == '__main__':
    n = int(input())

    start_time1 = timeit.default_timer()
    result = eratosthenes(n)
    end_time1 = timeit.default_timer()

    start_time2 = timeit.default_timer()
    result_2 = [number for number in range(2, n + 1) if prostoe(number)]
    end_time2 = timeit.default_timer()

    print('Простые числа')
    print(*[el for el in range(2, n + 1) if result[el]])
    print(*result_2)
    print(f"Вычисление (решето Эратосфена) заняло {end_time1 - start_time1} секунд")
    print(f"Вычисление (простой метод) заняло {end_time2 - start_time2} секунд")
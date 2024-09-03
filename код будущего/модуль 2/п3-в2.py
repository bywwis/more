import math
import timeit
import random
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

if __name__ == '__main__':

    a = random.randint(1000, 1000000)
    b = random.randint(1000, 1000000)

    start_time1 = timeit.default_timer()
    result1 = lcm(a, b)
    end_time1 = timeit.default_timer()

    start_time2 = timeit.default_timer()
    result2 = math.lcm(a, b)
    end_time2 = timeit.default_timer()

    print(f"Для чисел {a} и {b}:")
    print(f"Наименьшее общее кратное: {result1}, время работы: {end_time1 - start_time1} секунд")
    print(f"Работа функции math.gcd: {result2}, время работы: {end_time2 - start_time2} секунд")




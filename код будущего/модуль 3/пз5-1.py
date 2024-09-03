class Solver:
    __last_operation = None
    @staticmethod
    def add(x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            Solver.__last_operation = x + y
            return Solver.__last_operation
        return None

    @staticmethod
    def sub(x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            Solver.__last_operation = x - y
            return Solver.__last_operation
        return None

    @staticmethod
    def mult(x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            Solver.__last_operation = x * y
            return Solver.__last_operation
        return None

    @staticmethod
    def exp(x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            Solver.__last_operation = x ** y
            return Solver.__last_operation
        return None

    @staticmethod
    def div(x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)) and y != 0:
            Solver.__last_operation = x / y
            return Solver.__last_operation
        return None

    @staticmethod
    def int_div(x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)) and y != 0:
            Solver.__last_operation = x // y
            return Solver.__last_operation
        return None

    @staticmethod
    def rem(x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)) and y != 0:
            Solver.__last_operation = x % y
            return Solver.__last_operation
        return None

    @staticmethod
    def repeat():
        return Solver.__last_operation

if __name__ == '__main__':
    print(f'Сумма чисел 2 и 5: {Solver.add(2, 5)}')
    print(f'Разность чисел 2 и 5: {Solver.sub(2, 5)}')
    print(f'Произведение чисел 2 и 5: {Solver.mult(2, 5)}')
    print(f'2 в степени 2: {Solver.exp(2, 2)}')
    print(f'Результат деления 2 на 5: {Solver.div(2, 5)}')
    print(f'Результат целочисленного деления 2 на 5: {Solver.int_div(2, 5)}')
    print(f'Остаток от деления 2 на 5: {Solver.rem(2, 5)}')
    print(Solver.repeat())








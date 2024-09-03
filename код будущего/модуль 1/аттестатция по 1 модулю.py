class RomanToArabicAdapter:
    def __init__(self):
        self.roman_numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

    def convert(self, roman_number):
        result = 0
        prev_value = 0

        for char in reversed(roman_number):
            value = self.roman_numerals[char]
            if value < prev_value:
                result -= value
            else:
                result += value
                prev_value = value

        return result


class ArabicToRomanAdapter:
    def __init__(self):
        self.roman_mapping = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }

    def convert(self, arabic_number):
        result = ""
        for key, value in self.roman_mapping.items():
            while arabic_number >= key:
                result += value
                arabic_number -= key

        return result


def roman_to_arabic(roman_numbers):
    adapter = RomanToArabicAdapter()
    result = []
    for roman_number in roman_numbers.split(","):
        arabic_number = adapter.convert(roman_number.strip())
        result.append(f"{roman_number.strip()} -> {arabic_number}")
    return result


def arabic_to_roman(arabic_numbers):
    adapter = ArabicToRomanAdapter()
    result = []
    for arabic_number in arabic_numbers.split(","):
        roman_number = adapter.convert(int(arabic_number.strip()))
        result.append(f"{arabic_number.strip()} -> {roman_number}")
    return result


def evaluate_expression(expression):
    result = ""
    adapter = RomanToArabicAdapter()

    if '+' in expression:
        elements = expression.split("+")
        if elements[0].isdigit() and elements[1].isdigit():
            result = f"{elements[0]} + {elements[1]} = {int(elements[0]) + int(elements[1])}"
        else:
            arabic_first = adapter.convert(elements[0].strip())
            arabic_second = adapter.convert(elements[1].strip())
            result = f"{elements[0]} + {elements[1]} = {ArabicToRomanAdapter().convert(arabic_first + arabic_second)}"

    if '-' in expression:
        elements = expression.split("-")
        if elements[0].isdigit() and elements[1].isdigit():
            result = f"{elements[0]} - {elements[1]} = {int(elements[0]) - int(elements[1])}"
        else:
            arabic_first = adapter.convert(elements[0].strip())
            arabic_second = adapter.convert(elements[1].strip())
            result = f"{elements[0]} - {elements[1]} = {ArabicToRomanAdapter().convert(arabic_first - arabic_second)}"

    if '*' in expression:
        elements = expression.split("*")
        if elements[0].isdigit() and elements[1].isdigit():
            result = f"{elements[0]} * {elements[1]} = {int(elements[0]) * int(elements[1])}"
        else:
            arabic_first = adapter.convert(elements[0].strip())
            arabic_second = adapter.convert(elements[1].strip())
            result = f"{elements[0]} * {elements[1]} = {ArabicToRomanAdapter().convert(arabic_first * arabic_second)}"

    if '/' in expression:
        elements = expression.split("/")
        if elements[0].isdigit() and elements[1].isdigit():
            result = f"{elements[0]} / {elements[1]} = {int(elements[0]) / int(elements[1])}"
        else:
            arabic_first = adapter.convert(elements[0].strip())
            arabic_second = adapter.convert(elements[1].strip())
            result = f"{elements[0]} / {elements[1]} = {ArabicToRomanAdapter().convert(arabic_first / arabic_second)}"

    return result


if __name__ == "__main__":

    while True:
        print("Древнеримский калькулятор")
        print("Меню:")
        print("1. Перевод чисел из римских в арабские")
        print("2. Перевод чисел из арабских в римские")
        print("3. Вычисление выражения")
        print("4. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            roman_numbers = input("Введите римские числа через запятую: ")
            results = roman_to_arabic(roman_numbers)
            print("\n".join(results))

        elif choice == '2':
            arabic_numbers = input("Введите арабские числа через запятую: ")
            results = arabic_to_roman(arabic_numbers)
            print("\n".join(results))

        elif choice == '3':
            expression = input("Введите выражение (например, 5+3, I+I): ")
            try:
                result = evaluate_expression(expression)
                print(result)
            except ValueError:
                print("Ошибка: некорректное выражение")

        elif choice == '4':
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")


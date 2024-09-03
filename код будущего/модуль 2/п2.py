en_alphabet = {}
for i in range(1, 27):
    en_alphabet[chr(96+i)] = i
for key, value in en_alphabet.items():
    print(f"Ключ - буква {key}, значение - число {value}.")
login = input('Введите логин: ')
password = input('Введите пароль: ')
secret = input('Введите секретную строку: ')

secret_key = login[0::2] + password[1::2]

if secret_key == secret:
    print('correct')
else:
    print('incorrect')


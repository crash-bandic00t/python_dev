# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string

letterNumber = int(input('Введите номер буквы английского алфавита от 1 до 26 '))

cnt = 1
for i in string.ascii_lowercase: # итерируемся по буквам английского алфавита
    if cnt == letterNumber:
        print(f'Буква под номером "{letterNumber}" это буква "{i}"')
    cnt += 1

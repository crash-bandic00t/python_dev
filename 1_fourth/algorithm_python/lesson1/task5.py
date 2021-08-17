# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

import string

firstLetter = input('Введите букву английского алфавита для левой границы: ')
secondLetter = input('Введите букву английского алфавита для правой границы: ')

firstLetter = firstLetter.lower()
secondLetter = secondLetter.lower()

if ord(firstLetter) <= ord(secondLetter):
    cnt = 1
    for i in string.ascii_lowercase: # итерируемся по буквам английского алфавита
        if i == firstLetter:
            print(f'Место буквы "{firstLetter}" в алфавите = {cnt}')
            tmp1 = cnt
        elif i == secondLetter:
            print(f'Место буквы "{secondLetter}"" в алфавите = {cnt}')
            tmp2 = cnt 
        cnt += 1
    print(f'Между введенными буквами {tmp2 - tmp1 - 1} букв(ы,а)')
else:
    print('Некорректная граница букв')
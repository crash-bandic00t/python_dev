# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.


import random
 

intBoardLeft = int(input('Введите левую границу для целого числа: '))
intBoardRight = int(input('Введите правую границу для целого числа: '))

floatBoardLeft = float(input('Введите левую границу для вещественного числа: '))
floatBoardRight = float(input('Введите правую границу для вещественного числа: '))

symbolBoardLeft = ord(input('Введите левую границу для символа: '))
symbolBoardRight = ord(input('Введите правую границу для символа: '))


if intBoardLeft <= intBoardRight:
    print(f'Случайное целое число = {random.randint(intBoardLeft, intBoardRight)}')
else:
    print('Левая граница целых чисел должна быть меньше правой')

if floatBoardLeft <= floatBoardRight:
    print(f'Случайное вещественное число = {round(random.uniform(floatBoardLeft, floatBoardRight), 2)}')
else:
    print('Левая граница вещественных чисел должна быть меньше правой')

if symbolBoardLeft <= symbolBoardRight:
    print(f'Случайный символ = {chr(random.randint(symbolBoardLeft, symbolBoardRight))}')
else:
    print('Границы символов должны быть в алфавитно порядке')





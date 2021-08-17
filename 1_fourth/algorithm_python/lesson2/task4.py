# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элеметнов... '))

tmpList = []
flag = 0            # для определения с каким знаком добавлять в список число
tmpNumber = 2

while n != 0:
    tmpNumber /= 2
    if flag == 0:
        tmpList.append(tmpNumber)
        flag = 1
    elif flag == 1:
        tmpList.append(-tmpNumber)
        flag = 0
    n -= 1

print(f'Сумма элементов ряда чисел = {sum(tmpList)}')

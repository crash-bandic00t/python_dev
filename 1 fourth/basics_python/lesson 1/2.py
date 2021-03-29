# Сумма цифр числа
while True:
    sum = 0
    num = input('Введите число \n')
    if num == '0':
        break
    else:
        for i in num:
            sum += int(i)
        print(f'Сумма цифр числа {num} равна {sum}')
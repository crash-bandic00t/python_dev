# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

numbers = input('Введите натуральные числа через пробел: ')

listNumbers = numbers.split(' ')
dictionary = {}

for i in listNumbers:               # составляем словарь ключ - число, значение - сумма
    summa = 0
    for j in i:
        summa += int(j)
    dictionary[i] = summa

maxSumma = 0
for v in dictionary.values():     # определяем максимальную сумму
    if int(v) > maxSumma:
        maxSumma = int(v)

for k, v in dictionary.items():
    if v == maxSumma:
        print(f'Число {k}, сумма {v}')
        break




# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.


# Задача 6 из урока 2.
# Тут используется только 3 переменных одинакового типа, поэтому количество памяти, которое выделенно под них одинаковое
# import random
# import sys

# randomNumber = random.randint(0, 100)
# cnt = 1                                     # счетчик попыток
# number = int(input('Угадайте число! '))
# print(f'{sys.getsizeof(randomNumber) = }, {sys.getsizeof(number) = }')
# while True:
#     if cnt == 10:
#         print(f'Вы проиграли! Загаданное число "{randomNumber}"')
#         break
#     else:
#         if number > randomNumber:
#             print('Вы ввели слишком большое число.')
#         elif number < randomNumber:
#             print('Вы ввели слишком маленькое число.')
#         elif number == randomNumber:
#             print('Вы угадали!')
#             break
#         print(f'У вас осталось {10 - cnt} попыток')
#         number = int(input('Введите еще раз... '))
#         cnt += 1


#  Задача 9 из урока 2
# Тут судя по изменению размера sys.getsizeof наших элементов можно сказать, что объем памяти выделяемый под список увеличиватеся в случае количества элементов > 12
# А объем памяти под словарь увеличивается как от количества находящихся в нем элементов, так и от значений, которые получаются в результате работы программы.
# numbers = input('Введите натуральные числа через пробел: ')

# listNumbers = numbers.split(' ')
# dictionary = {}

# for i in listNumbers:               # составляем словарь ключ - число, значение - сумма
#     summa = 0
#     for j in i:
#         summa += int(j)
#     dictionary[i] = summa

# maxSumma = 0
# for v in dictionary.values():     # определяем максимальную сумму
#     if int(v) > maxSumma:
#         maxSumma = int(v)

# for k, v in dictionary.items():
#     if v == maxSumma:
#         print(f'Число {k}, сумма {v}')
#         break
# print(f'{sys.getsizeof(listNumbers) = }, {sys.getsizeof(dictionary) = }')
"""
Написать функцию-генератор rand_nums, генерирующую N случайных целых чисел в диапазоне 1 до 100 (включительно). Количество чисел N, которое выдаст генератор передается в функцию через параметр:

# >>> rand15 = rand_nums(15)
# >>> next(rand15) # 1-й вызов
11
# >>> next(rand15) # 2-й вызов
38
...
# >>> next(rand15) # 15-й вызов
7
# >>> next(rand15) # 16-й вызов
...StopIteration...
"""

from random import randrange



def rand_nums(cnt):
    for i in range(cnt):
        rand_num = randrange(101)
        yield rand_num
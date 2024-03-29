"""
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
"""

import time


start = time.perf_counter()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 11]
result = set()
tmp = set()

for i in src:
    if i not in tmp:
        result.add(i)
    else:
        result.discard(i)
    tmp.add(i)

# print(perf_counter() - start)
result_ord = [i for i in src if i in result]
print(result_ord)
print(time.perf_counter() - start)
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

lst = [105, 8, 3, 0, 6, 4, 2, 200, 2]
lst.sort()                              # сортируем список и выводим 2 первых элемента
print(lst[:2])

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

lst = [8, 3, 84, 15, 6, 4, 2]

for e, number in enumerate(lst):    # находим индексы мин. и макс. элемента списка
    if number == max(lst):
        maxIndex = e
    elif number == min(lst):
        minIndex = e

lst[maxIndex], lst[minIndex] = lst[minIndex], lst[maxIndex]     # меняем их местами

print(lst)
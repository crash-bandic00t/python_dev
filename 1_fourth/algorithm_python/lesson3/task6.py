# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

lst = [105, 8, 3, 0, 6, 4, 2, 200, 2]

for e, number in enumerate(lst):        # находим индексы мин. и макс. элементов
    if number == max(lst):
        maxIndex = e
    elif number == min(lst):
        minIndex = e

if minIndex > maxIndex:                 # расставляем индексы в правильном порядке
    print(f'Сумма между макс. и мин. элементом равна {sum(lst[maxIndex + 1:minIndex])}')
else:
    print(f'Сумма между макс. и мин. элементом равна {sum(lst[minIndex + 1:maxIndex])}')



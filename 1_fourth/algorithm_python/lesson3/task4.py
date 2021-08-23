# Определить, какое число в массиве встречается чаще всего.

lst = [15, 8, 3, 84, 6, 4, 2, 15, 2]
maxCount = 0

for e, number in enumerate(lst):        # считаем число вхождений каждого элемента и находим максимум
    cnt = lst.count(number)
    if cnt > maxCount:
        maxCount = cnt
        maxNumberIndex = e              # запомнили на каком месте он стоит и вывели в консоль


print(f'Чаще всего встречается число {lst[maxNumberIndex]}')
    
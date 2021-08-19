# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.



# Проверка что числа из диапазона 2-99 делятся на 2-9 одновременно
lst = []
for i in range(2, 100):         # заполняем список числами от 2 до 99
    lst.append(i)

lstMultiple = [2, 3, 4, 5, 6, 7, 8, 9]

result = []

for i in lst:                   # проверяем кратность
    for j in lstMultiple:
        if i % j == 0:
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        result.append(i)

print(result)

# Проверка сколько из чисел 2-99 кратны числам в диапазоне 2-9 (без слова каждому)
resultDict = {}

for i in lst:
    for j in lstMultiple:
        if i % j == 0:
            resultDict[j] = resultDict.setdefault(j, 0) + 1

print(resultDict)
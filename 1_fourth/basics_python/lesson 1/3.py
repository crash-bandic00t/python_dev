# Сумма чисел из списка
# Задание 3.1
list = []
for i in range(1000):
    if i % 2 == 1:
        list.append(i**3)
sumList = 0
for i in list:
    sum = 0
    for j in str(i):
        sum += int(j)
    if sum % 7 == 0:
        sumList += i
print(f'Сумма чисел, сумма цифр которых делится нацело на 7 равна {sumList}')


# Задание 3.2
newList = []
for i in list:
    newList.append(i + 17)
sumListNew = 0
for i in newList:
    sum = 0
    for j in str(i):
        sum += int(j)
    if sum % 7 == 0:
        sumListNew += i   
print(f'Сумма чисел нового списка, где каждый элемент увеличен на 17, сумма цифр которых делится нацело на 7 равна {sumListNew}')

# Задание 3.3
sumList = 0
for i in range(1000):
    if i % 2 == 1:
        i = i**3 + 17
        sum = 0
        for j in str(i):
            sum += int(j)
        if sum % 7 == 0:
            sumList += i
print(f'Сумма чисел как в задании 3.2, без использования списков равна {sumList}')



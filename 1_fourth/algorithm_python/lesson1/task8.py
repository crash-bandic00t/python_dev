# Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = int(input('Введите год: '))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('Год високосный')
else:
    print('Год обычный')


import calendar
print(calendar.isleap(year)) # чтобы не изобретать велосипед))
#  Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input('Введите число: '))
tmp = map(int, str(number))
summary = 0
mult = 1

for i in tmp:
    summary += i
    mult *= i

print(f'Сумма равна {summary}, произведение равно {mult}')
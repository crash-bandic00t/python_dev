# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


numbers = input('Введите числа через пробел: ')

print(hex(int(f'0x{numbers.split()[0]}', 16) + int(f'0x{numbers.split()[1]}', 16))) # переводим числа в int dec из hex, проводим операции сложения и умножения и переводим обратно в hex
print(hex(int(f'0x{numbers.split()[0]}', 16) * int(f'0x{numbers.split()[1]}', 16)))
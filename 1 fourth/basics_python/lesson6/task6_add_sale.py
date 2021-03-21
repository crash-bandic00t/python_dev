import sys
import json


# Решение для хранения данных в виде json.
# Для записи в файл оно более ёмкое, зато при чтении можно легко итерироваться по списку.
# Однако для реализации 7 задания такой вариант хранения продаж не подходит, либо я не понял как вытащить конкретное значение из списка не читая его полностью.
"""
if len(sys.argv) > 1:
    with open('bakery.csv', 'r+') as add:
        update = add.readline().strip()
        if update == '':
            update_summ = [sys.argv[1]]
        else:
            update_summ = json.loads(update)
            update_summ.append(sys.argv[1])
        add.seek(0)
        add.truncate()
        add.write(json.dumps(update_summ))
else:
    print('Введите сумму продаж')
"""



# Решение, храня данные построчно. Подходит для выполнения задания 7.
if len(sys.argv) > 1:
    with open('bakery.csv', 'a') as add:
        add.write(f'{sys.argv[1]}\n')
else:
    print('Введите сумму продаж')

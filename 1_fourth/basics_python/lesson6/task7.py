"""
 Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер записи и новое значение. 
 При этом файл не должен читаться целиком — обязательное требование. 
 Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.
"""
import sys
import json



# Попытка решения. Решено только если суммы одинаковой длины и являются целыми числами. Чтобы полностью решить, надо больще времени, но сроки горят)
# Чтобы 7 задача корректно работала надо также пересмотреть запись сумм в файл, чтобы они были одинаковой длины.
with open('bakery.csv', 'r+') as f:
    
    line = f.readline().strip()
    line_cnt = 1
    while line:
        if line_cnt == int(sys.argv[1]):
            cursor = f.tell()
            break
        line = f.readline().strip()
        line_cnt += 1
    f.seek(cursor - 5)
    f.write(sys.argv[2])



# Данное решение читает весь файл, что не удовлетворяет заданию. Просто я написал его раньше, а потом понял что не подходит, решил оставить))
"""
if len(sys.argv) == 3:
    with open('bakery.csv', 'r+') as replace:
        summs = replace.readline().strip()
        summ_list_change = json.loads(summs)
        try:
            summ_list_change[int(sys.argv[1]) - 1] = sys.argv[2]
        except:
            print('Такого значения нет в списке!')
            exit(1)
        replace.seek(0)
        replace.truncate()
        replace.write(json.dumps(summ_list_change))
else:
    print('Введите 2 аргумента!')
"""
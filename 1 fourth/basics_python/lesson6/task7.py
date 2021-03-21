"""
 Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер записи и новое значение. 
 При этом файл не должен читаться целиком — обязательное требование. 
 Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.
"""
import sys
import json
from itertools import islice


#Решение не читая весь файл не смог осилить.
# if len(sys.argv) == 3:
#     with open('bakery.csv', 'r+') as replace:
#         line_cnt = 1
#         for line in replace:
#             print(replace.tell())
#             if line_cnt == int(sys.argv[1]):
#                 line = f'{sys.argv[2]}\n'
#                 replace.write(line)
#                 print(replace.tell())
#                 line_cnt += 1
#             else:
#                 line_cnt += 1

with open('bakery.csv', 'r+') as replace:
    line = replace.readline().strip()
    while line:
        cursor = replace.tell()
        replace.seek(cursor)
        replace.write('333')        
        line = replace.readline().strip()



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
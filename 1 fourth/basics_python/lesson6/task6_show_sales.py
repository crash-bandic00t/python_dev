import sys
import json

# Решение, если бы данные хранились в виде списка. Несколько короче чем с построчным хранением.
# Не подходит для больших файлов.
"""
if len(sys.argv) == 1:
    with open('bakery.csv') as show:
        show_summ = show.readline().strip()
        summ_list = json.loads(show_summ)
        for summ in summ_list:
            print(summ)
elif len(sys.argv) == 2:
    with open('bakery.csv') as show:
        show_summ = show.readline().strip()
        summ_list = json.loads(show_summ)
        for summ in summ_list[int(sys.argv[1]) - 1:]:
            print(summ)
elif len(sys.argv) == 3:
    with open('bakery.csv') as show:
        show_summ = show.readline().strip()
        summ_list = json.loads(show_summ)
        for summ in summ_list[int(sys.argv[1]) - 1:int(sys.argv[2])]:
            print(summ)
else:
    print('Введите 2 аргумента!')
"""

            
# Решение, если бы данные хранились построчно. Подходит для больших файлов.
if len(sys.argv) == 1:
    with open('bakery.csv') as show:
        for line in show:
            print(line.strip())
elif len(sys.argv) == 2:
    line_cnt = 1
    with open('bakery.csv') as show:
        for line in show:
            if line_cnt >= int(sys.argv[1]):
                print(line.strip())
                line_cnt += 1
            else:
                line_cnt += 1
elif len(sys.argv) == 3:
    line_cnt = 1
    with open('bakery.csv') as show:
        for line in show:
            if line_cnt >= int(sys.argv[1]) and line_cnt <= int(sys.argv[2]):
                print(line.strip())
                line_cnt += 1
            else:
                line_cnt += 1
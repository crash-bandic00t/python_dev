"""
Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом командной строки: 
для записи данных и для вывода на экран записанных данных. При записи передавать из командной строки значение суммы продаж. 
Для чтения данных реализовать в командной строке следующую логику:
. просто запуск скрипта — выводить все записи;
. запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
. запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму числу, включительно.
Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:

python add_sale.py 5978,5
python add_sale.py 8914,3
python add_sale.py 7879,1
python add_sale.py 1573,7
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
7879,1
"""
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
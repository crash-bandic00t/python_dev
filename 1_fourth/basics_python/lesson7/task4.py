"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""
import os


d = {}
path_from = r'f:\GeekBrains\python_dev\1_fourth\basics_python\lesson7'
for root, folders, files in os.walk(path_from):
    for file_name in files:
        path_final = os.path.join(root, file_name)
        if os.path.isfile(path_final):
            d.setdefault(10 ** len(str(os.stat(path_final).st_size)), 0)
            d[10 ** len(str(os.stat(path_final).st_size))] += 1

print(d)
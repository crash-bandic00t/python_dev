"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""
import os
import json


d = {}
path_from = r'f:\GeekBrains\python_dev\1_fourth\basics_python\lesson7'
for root, folders, files in os.walk(path_from):
    for file_name in files:
        path_final = os.path.join(root, file_name)
        file_size = os.stat(path_final).st_size
        if os.path.isfile(path_final): 
            d.setdefault(10 ** len(str(file_size)), [0, set()])
            d[10 ** len(str(file_size))][0] += 1
            d[10 ** len(str(file_size))][1].add(path_final.split('\\')[-1].split('.')[-1])
            
for key, val in d.items():
    d[key][1] = list(d[key][1])

with open('templates_summary.json', 'w') as f:
    f.write(json.dumps(d))
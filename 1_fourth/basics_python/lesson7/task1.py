"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
"""
import os


dir_list = ['settings','mainapp','adminapp','authapp']

for i in dir_list:
    os.makedirs(f'my_project\{i}')
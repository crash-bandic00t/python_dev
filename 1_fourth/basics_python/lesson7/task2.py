"""
Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""
import os


with open(r'1_fourth\basics_python\lesson7\config.yaml') as f:
    path = None
    for line in f:
        if '[' in line and not path:
            path = line.strip().split(':')[0]
            os.mkdir(path)
        elif '[' in line and path:
            path = f'{path}\{line.strip().split(":")[0]}'
            os.mkdir(path)
        elif ']' in line:
            path = '\\'.join(path.split('\\')[:-1])
        else:
            with open(f'{path}\\{line.strip()}', 'w') as new_f:
                pass
"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; 
это реальная задача, которая решена, например, во фреймворке django.
"""
import os
import shutil


for root, dirs, files in os.walk(r"f:\GeekBrains\python_dev\1_fourth\basics_python\lesson7\my_project"):
    for dir_name in dirs:
        if dir_name == 'templates':
            shutil.copytree(f'{root}\\templates', r'f:\GeekBrains\python_dev\1_fourth\basics_python\lesson7\my_project\templates', dirs_exist_ok=True)
            
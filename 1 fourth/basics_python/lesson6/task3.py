"""
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. 
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл. Проверить сохранённые данные. 
Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». 
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""
import json


users = open('e:\\GeekBrains\\python_dev\\1 fourth\\basics_python\\lesson6\\users.csv', encoding='utf-8')
hobbies = open('e:\\GeekBrains\\python_dev\\1 fourth\\basics_python\\lesson6\\hobby.csv', encoding='utf-8')
users_hobby = {}
user = users.readline().strip()
hobby = hobbies.readline().strip()
while user:
    if hobby:
        users_hobby.setdefault(user, hobby)
    else:
        users_hobby.setdefault(user, None)        
    user = users.readline().strip()
    hobby = hobbies.readline().strip()
if hobby:
    exit(1)
users.close()
hobbies.close()
with open('e:\\GeekBrains\\python_dev\\1 fourth\\basics_python\\lesson6\\users_hobby_task3.json', 'w', encoding='utf-8') as uh: #Передаю в словарь через сериализатор. Так как иначе сделать словарь просто так не получится
    uh.write(json.dumps(
        users_hobby, 
        ensure_ascii=False, 
        indent=4,
        )
    )


"""
Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта). 
Также реализовать парсинг данных из файлов - получить отдельно фамилию, имя и отчество для пользователей 
и название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь). 
Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге. В словаре должны храниться данные, полученные в результате парсинга.
"""
import json


users = open('e:\\GeekBrains\\python_dev\\1 fourth\\basics_python\\lesson6\\users.csv', encoding='utf-8')
hobbies = open('e:\\GeekBrains\\python_dev\\1 fourth\\basics_python\\lesson6\\hobby.csv', encoding='utf-8')
users_hobby = {}
user = users.readline().strip()
hobby = hobbies.readline().strip()
while user:
    if hobby:
        users_hobby.setdefault(user.replace(',', ' '), hobby.split(','))
    else:
        users_hobby.setdefault(user.replace(',', ' '), None)        
    user = users.readline().strip()
    hobby = hobbies.readline().strip()
if hobby:
    exit(1)
users.close()
hobbies.close()
with open('e:\\GeekBrains\\python_dev\\1 fourth\\basics_python\\lesson6\\users_hobby_task4.json', 'w', encoding='utf-8') as uh: #Передаю в словарь через сериализатор. Так как иначе сделать словарь просто так не получится
    uh.write(json.dumps(
        users_hobby, 
        ensure_ascii=False, 
        indent=4,
        )
    )

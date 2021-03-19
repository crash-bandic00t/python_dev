import sys
import json

if len(sys.argv) > 1:
    users = open(sys.argv[1], encoding='utf-8')
    hobbies = open(sys.argv[2], encoding='utf-8')
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
    with open(sys.argv[3], 'w', encoding='utf-8') as uh: #Передаю в словарь через сериализатор. Так как иначе сделать словарь просто так не получится
        uh.write(json.dumps(
            users_hobby, 
            ensure_ascii=False, 
            indent=4,
            )
        )

else:
    print('Вы не ввели пути, где хранятся файлы')

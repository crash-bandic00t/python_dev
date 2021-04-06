"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. 
Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
"""

import re


d = {}
def email_parse(mail):
    result = re.search(r'\w+@\w+\.\w+', mail)
    if result is not None:
        mail = mail.split('@')
        d.setdefault('username', mail[0])
        d.setdefault('domain', mail[1])
        return d
    else:
        msg = f'wrong email: {mail}'
        raise ValueError(msg)

print(email_parse('loot@gmail.com'))
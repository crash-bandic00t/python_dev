"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

edited_log = open('nginx_edited.txt', 'a', encoding='utf-8')
with open('nginx_logs.txt') as log:
    for line in log:
        log_string = line.strip()
        ip_address = log_string.split(' - -')[0]
        log_detatil = log_string.split('] "')[1].split('" ')[0].split()
        edited_log.write(f'{ip_address}, {log_detatil[0]}, {log_detatil[1]}\n')
edited_log.close()


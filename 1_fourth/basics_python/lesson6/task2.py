"""
Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

addresses = {}
with open('nginx_edited.txt') as log:
    for line in log:
        ip_address = line.strip().split(',')[0]
        if ip_address not in addresses:
            addresses.setdefault(ip_address, 1)
        else:
            addresses[ip_address] += 1
max_val = max(addresses.values())
for k,v in addresses.items():
    if v == max_val:
        print(f'Спамером является адрес: {k}. Количество запросов равно: {v}')
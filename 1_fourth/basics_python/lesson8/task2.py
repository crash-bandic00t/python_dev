"""Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения информации вида: 
(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>), например:

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
"""
import re

pattern = re.compile(r'((?:(?:\d{1,3}\.){3}\d{1,3}|(?:\w{1,4}\:){7}\w{1,4}))[^[]*\[(.*)\][^\"]*\"([A-Z]+)\s(\/[^\s]+)\s[^ ]*\s(\d+)\s(\d+)')
parsed_logs = open('nginx_parsed.txt', 'w')
with open('nginx_logs.txt') as f:
    for line in f:
        line_raw = f.readline().strip()
        line_parsed = pattern.findall(line_raw)
        parsed_logs.write(f'{str(*line_parsed)}\n')
parsed_logs.close()


# line = '54.247.176.246 - - [24/May/2015:06:05:33 +0000] "GET /downloads/product_1 HTTP/1.1" 200 2575 "-" "urlgrabber/3.9.1 yum/3.4.3"'
# result = re.search(r'(\w{1,4}\.\w{1,4}\.\w{1,4}\.\w{1,4}|\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}).*\[(.*)\] "(\w+) (/.*) HTTP.*" (\d+) (\d+)', line)
# print(result.group(6))
# \w{1,4}\.\w{1,4}\.\w{1,4}\.\w{1,4}|\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}
# result = re.search(r'(\w{1,4}\.\w{1,4}\.\w{1,4}\.\w{1,4}|\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}).*\[(.*)\] "(\w+) (/.*) HTTP.*" (\d+) (\d+)', line)
# line = '188.138.60.101.'
# result = re.search(r'(?:\d{1,3}\.){4}', line)
# print(result)

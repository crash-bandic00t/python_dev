"""
Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли,
а коды валют ему дожны передавать через аргументы командной строки (там может быть один или несколько кодов).
Вывод курсов сделать в том же порядке, что присланные аргументы
Например:

python task5.py USD EUR
USD 75.18, 2020-09-05
EUR 80.35, 2020-09-05
"""


from utils import get_currency_rate
import sys

if len(sys.argv) > 1:
    for i in range(len(sys.argv) - 1):
        get_currency_rate(sys.argv[i+1])
else:
    print('Вы не ввели агрументов, поэтому вот вам курс доллара и евро:')
    get_currency_rate('USD')
    get_currency_rate('eur')

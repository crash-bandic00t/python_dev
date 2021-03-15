"""
Доработать функцию get_currency_rate(): теперь она должна возвращать курс и дату,
на которую этот курс действует (взять из того же файла ЦБ РФ).
Для значения курса используйте тип Decimal (https://docs.python.org/3.8/library/decimal.html) вместо float.
Дата должна быть типа datetime.date.
"""

from requests import get
from bs4 import BeautifulSoup
import datetime
from decimal import Decimal


def get_currency_rate(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    soup = BeautifulSoup(response.text, 'html.parser')
    currency_codes = []
    all_valute = soup.find_all('valute')
    date = soup.valcurs['date'].split('.')

    for valute in all_valute:
        currency_codes.append(valute.charcode.text)
        if valute.charcode.text == currency.upper():
            currency_value = Decimal(valute.value.text.replace(",","."))
            print(f'{valute.charcode.text} {currency_value.quantize(Decimal("1.00"))}, {datetime.date(int(date[2]), int(date[1]), int(date[0]))}')


    if currency.upper() not in currency_codes:
        print('None')

get_currency_rate('USD')
get_currency_rate('EUR')
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

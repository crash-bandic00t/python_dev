"""
Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
Код валюты может быть в произвольном регистре.
Функция должна возвращать результат числового типа, например float.
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
http://www.cbr.ru/scripts/XML_daily.asp.

Выведите на экран курсы для доллара и евро, используя написанную функцию.

Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере, посмотреть содержимое ответа.
"""


from requests import get
from bs4 import BeautifulSoup


def get_currency_rate(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    soup = BeautifulSoup(response.text, 'html.parser')
    currency_codes = []
    all_valute = soup.find_all('valute')

    for valute in all_valute:
        currency_codes.append(valute.charcode.text)
        if valute.charcode.text == currency.upper():
            currency_value = float(valute.value.text.replace(",","."))
            print(f'{valute.charcode.text} {format(currency_value, ".2f")}')

    if currency.upper() not in currency_codes:
        print('None')

get_currency_rate('USD')
get_currency_rate('EUR')
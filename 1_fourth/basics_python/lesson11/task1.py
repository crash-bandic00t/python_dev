"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
import datetime


class Date:

    def __init__(self, date):
        self.date = self.parse_date(date)
    
    @classmethod
    def parse_date(cls, date):
        result = list(map(int, date.split('-')))
        return result
    
    @staticmethod
    def check_date(date):
        if date[0] not in range(1,32):
            return 'Некорректная дата'
        elif date[1] not in range(1,13):
            return 'Некорректная дата'
        else:
            return 'Дата корректна'



a = Date('32-12-2021')
print(a.check_date(a.date))

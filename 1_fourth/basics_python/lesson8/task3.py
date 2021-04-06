"""
Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

# >>> a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""
from functools import wraps



def type_logger(func):

    @wraps(func)
    def inner(*args, **kwargs):
        list_of_types = []
        for i in args:
            list_of_types.append(f'{i}: {type(i)}')
        for k,v in kwargs.items():
            list_of_types.append(f'{k}={v}: {type(v)}')
        return list_of_types
    return inner

@type_logger
def calc_cube(x):
    return x ** 3

print(f'{calc_cube.__name__}{calc_cube(5)}')
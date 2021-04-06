"""
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


# >>> a = calc_cube(5)
125
# >>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
"""
from functools import wraps


def val_checker(decor_func):
    def my_decorator(func):
        def inner(y):
            if decor_func(y):
                return func(y)
            elif not decor_func(y):
                msg = f'wrong val {y}'
                raise ValueError(msg)
        return inner
    return my_decorator

@val_checker(lambda x: x > 0)    
def calc_cube(x):
   return x ** 3

print(calc_cube(-2))
"""
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
...
@val_checker(lambda x: x > 0)
def calc_cube(x):
return x ** 3
>>> a = calc_cube(5)
125
>>> a = calc_cube(-5)
Traceback (most recent call last):
raise ValueError(msg)
"""

from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # result = func(*args, **kwargs)
        result = []
        try:
            for i in list(args) + list(kwargs.values()):
                result.append(int(i) / 3)
            print('\tcall {} {}'.format(func.__name__, list(map(lambda x: type(x), list(args) + list(kwargs.values())))))
        except Exception as exp:
            raise ValueError(f'ValueError: invalid arguments passed: {list(args) + list(kwargs.values())}')
        return result

    return wrapper


@type_logger
def calc_cube(*args, **kwargs):
    res = []
    for i in list(args) + list(kwargs.values()):
        res.append(int(i) ** 3)
    return res


a = calc_cube(5, 4, 6, a=2, d='s')
print(a)

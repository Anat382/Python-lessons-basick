"""
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
...
@type_logger
def calc_cube(x):
return x ** 3
>>> a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете
ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя
функции, например, в виде:
"""
from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # result = func(*args, **kwargs)
        result = []
        for i in list(args) + list(kwargs.values()):
            result.append(int(i) / 3)
        print('\tcall {} {}'.format(func.__name__, list(map(lambda x: type(x), list(args) + list(kwargs.values())))))
        return result

    return wrapper


@type_logger
def calc_cube(*args, **kwargs):
    res = []
    for i in list(args) + list(kwargs.values()):
        res.append(int(i) ** 3)
    return res


a = calc_cube(5, 4, 6, a=2, d=3)
print(a)

"""
### 1. Реализовать
 вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
 до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях:
  <d> дн <h> час <m> мин <s> сек.
Примеры:

duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек

Примечание: можете проверить себя здесь, подумайте, можно ли использовать цикл для проверки работы кода сразу
для нескольких значений продолжительности, будет ли тут полезен список?
"""


# цикл в данной задачаче не нужен


def convert_day(sec=0):
    day_ = int(sec // 3600 // 24)
    return day_ if day_ != 0 else '00'


def convert_hour(sec=0):
    hour_ = int(sec / 3600 // 1)
    return hour_ if hour_ != 0 else '00'


def convert_minute(sec=0):
    minute_ = int(sec / 3600 % 1 * 60 // 1)
    return minute_ if minute_ != 0 else '00'


def convert_second(sec=0):
    second_ = round(sec / 3600 % 1 * 60 % 1 * 60)
    return second_ if second_ != 0 else '00'


duration = int(input('Введите секунды: '))
sec24 = 86400

if duration >= sec24:  # day
    day_ = convert_day(duration)
    hour_ = convert_hour(duration)
    minute_ = convert_minute(duration)
    sec = convert_second(duration)
    print(f'{day_} дн {hour_} час {minute_} мин {sec} сек')
else:
    hour_ = convert_hour(duration)
    minute_ = convert_minute(duration)
    sec = convert_second(duration)
    print(f'{hour_} час {minute_} мин {sec} сек')

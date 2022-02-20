"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый — с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""

import re
from datetime import datetime


class Date:
    def __init__(self, test_date):
        self.test_date = test_date

    def __str__(self):
        return str(self.test_date)

    @classmethod
    def take_part_date(cls, test_date):
        cls.test_date = test_date
        res = re.findall(r'\d{2}\-\d{2}\-\d{4}', cls.test_date)
        assert res, "Не корректный формат даты, шаблон(DD-MM-YYYY)"
        day_, month_, year_ = int(cls.test_date[:2]), int(cls.test_date[3:5]), int(cls.test_date[6:])
        return [day_, month_, year_]

    @staticmethod
    def check_number(test_date):
        day_, month_, year_ = test_date[0], test_date[1], test_date[2]
        assert day_ <= 31, f'{day_} больше максимального кол-ва дней в мeсяце - {31}'
        assert month_ <= 12, f'{month_} больше максимального кол-ва месяцев в году - {12}'
        assert year_ <= datetime.now().year, f'{year_} больше текущего - {datetime.now().year}'


inter_data = Date('31-12-2022').__str__()
part_dates = Date.take_part_date(inter_data)
print(part_dates)

Date.check_number(part_dates)

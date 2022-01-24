"""
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
Использовать библиотеку requests. В качестве API можно использовать
http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API
в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса
str, решить поставленную задачу? Функция должна возвращать результат числового типа,
например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера
выведите курсы доллара и евро.

"""

from requests import get


def currency_rates(*args):
    """
    get rate
    :param args:
    :return:
    """
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = get(url)
    rate_list = []
    if response.status_code == 200:
        # print(response.status_code)
        content = response.content.decode(encoding=response.encoding)
        # print(content)
        cur_list = list(map(lambda x: str(x).upper(), list(args)))
        # print(cur_list)
        for elem in cur_list:
            rate = None
            for el in content.split('<CharCode>')[1:]:
                # print(el.split('<')[0])
                for i in el.split('<'):
                    if 'Value>' in i and '/' not in i and el.split('<')[0] == elem:
                        rate = float(i.split('Value>')[1].replace(',', '.'))
            rate_list.append(rate)
        return rate_list
    else:
        raise BaseException("No connection, status code response ", response.status_code)


print(currency_rates('USD', 'CHF', 'ru'))

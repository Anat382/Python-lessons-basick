"""
*(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса
дату, которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте,
как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
"""

from requests import get
import datetime


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
                # print(el.split('<'), content.split("ValCurs Date=")[1][1:11])
                for i in el.split('<'):
                    if 'Value>' in i and '/' not in i and el.split('<')[0] == elem:
                        rate = (float(i.split('Value>')[1].replace(',', '.')))
            rate_list.append(rate)
        return datetime.date.fromisoformat(content.split("ValCurs Date=")[1][7:11] + '-' +
                                           content.split("ValCurs Date=")[1][4:6] + '-' +
                                           content.split("ValCurs Date=")[1][1:3]), rate_list
    else:
        raise BaseException("No connection, status code response ", response.status_code)


if __name__ == '__main__':
    print(currency_rates('USD', 'CHF', 'ru'))


from requests import get
import datetime


# currency_rates
def main(argv):
    """
    get rate
    :param argv:
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
        program,  *args = argv
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
    import sys

    exit(main(sys.argv))

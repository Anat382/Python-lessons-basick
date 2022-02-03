"""
2. *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6
урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs
) для получения информации вида: (<remote_addr>, <request_datetime>,
<request_type>, <requested_resource>, <response_code>, <response_size>),
например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET
/downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET',
'/downloads/product_2', '304', '0')
Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
"""

import re
from time import perf_counter

start = perf_counter()
my_log = []
with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    for i in f:
        my_log.append((i.split('-')[0].strip(), i.split('/')[2][-4:].strip(),
                       i.split(']')[1].split('HTTP')[0][5:].strip()))

# print(list(set(my_log)))
print(perf_counter() - start)

start = perf_counter()
reg_exp_ip = re.compile(r'^(\d+\.\d+\.\d+\.\d+)[ - -$]|^(\w+\S+\w+\S+\w+\S+\w+\S+\w+\S+\w+\S+\w+\S+\w+)[ - -$]')
reg_exp_type = re.compile(r'"(\w+)\s[/$]')
reg_exp_folder = re.compile(r'\s\/(\w+\/\w+)')

my_log_reg = []
c = 0
with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    for i in f:
        my_log_reg.append(( re.match(reg_exp_ip, i).group(0).strip(), re.findall(reg_exp_type, i)[0],
                        re.findall(reg_exp_folder, i)[0]))

print(perf_counter() - start)
print(list(set(my_log_reg)))
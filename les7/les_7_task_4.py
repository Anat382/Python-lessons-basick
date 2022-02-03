"""
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее
количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
но больше предыдущей (начинаем с 0), например:
{
100: 15,
1000: 3,
10000: 7,
100000: 2
}
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

import os

my_folder = r'E:/Mail_ru geekbrains DATAINGENEER/Основы языка Python/git_lesson'

stat_ram = {}

count_100 = 0
count_1000 = 0
count_10000 = 0
count_100000 = 0

for root, dirr, files in os.walk(my_folder):
    for file in files:
        file_size = os.path.getsize(os.path.join(str(root), file))
        if file_size <= 100:
            count_100 += 1
            stat_ram['100'] = count_100
        elif 100 < file_size <= 1000:
            count_1000 += 1
            stat_ram['1000'] = count_1000
        elif 1000 < file_size <= 10000:
            count_10000 += 1
            stat_ram['10000'] = count_10000
        else:
            count_100000 += 1
            stat_ram['100000'] = count_100000

print(dict(sorted(stat_ram.items(), key=lambda x: x[0])))

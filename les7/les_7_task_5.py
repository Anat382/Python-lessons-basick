"""
5. *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи те же, а значения — кортежи вида (<files_quantity>,
[<files_extensions_list>]), например:
{
100: (15, ['txt']),
1000: (3, ['py', 'txt']),
10000: (7, ['html', 'css']),
100000: (2, ['png', 'jpg'])
}
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили
скрипт.
"""


import os

my_folder = r'E:/Mail_ru geekbrains DATAINGENEER/Основы языка Python/git_lesson'

stat_ram = {}

count_100 = 0
count_1000 = 0
count_10000 = 0
count_100000 = 0

ext_100 = []
ext_1000 = []
ext_10000 = []
ext_100000 = []

for root, dirr, files in os.walk(my_folder):
    for file in files:
        extension = file.split('.')[-1]
        file_size = os.path.getsize(os.path.join(str(root), file))
        if file_size <= 100:
            ext_100 += [extension]
            count_100 += 1
            stat_ram['100'] = (count_100, list(set(ext_100)))
        elif 100 < file_size <= 1000:
            ext_1000 += [extension]
            count_1000 += 1
            stat_ram['1000'] = (count_1000, list(set(ext_1000)))
        elif 1000 < file_size <= 10000:
            ext_10000 += [extension]
            count_10000 += 1
            stat_ram['10000'] = (count_10000, list(set(ext_10000)))
        else:
            ext_100000 += [extension]
            count_100000 += 1
            stat_ram['100000'] = (count_100000, list(set(ext_100000)))

print(dict(sorted(stat_ram.items(), key=lambda x: x[0])))


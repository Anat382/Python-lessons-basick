"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""

import sys
import json


users = [
    'Иванов,Иван,Иванович\n',
    'Петров,Петр,Петрович'
]

hobby = [
    'скалолазание,охота\n', 'горные лыжи\n'  # ,'горные лыжи'
]

with open('users.csv', 'w', encoding='utf-8') as f:
    f.writelines(users)

with open('hobby.csv', 'w', encoding='utf-8') as f:
    f.writelines(hobby)

users = []
with open('users.csv', 'r', encoding='utf-8') as f:
    for i in f:
        users.append(i.replace('\n', ''))

hobby = []
with open('hobby.csv', 'r', encoding='utf-8') as f:
    for i in f:
        hobby.append(i.replace('\n', ''))


count_users = len(users)
count_hobby = len(hobby)
difcount = abs(count_hobby-count_users)

if count_hobby < count_users:
    for _ in range(difcount):
        hobby += [None]
elif count_hobby > count_users:
    sys.exit(1)

# print(users, hobby)

with open('users_hobby.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(dict(zip(users, hobby))))

with open('users_hobby.json', 'r', encoding='utf-8') as f:
    nums_as_str = f.read()
users_hobby = json.loads(nums_as_str)
print(users_hobby)

"""
4. *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём
ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на
будущее проекта). Только теперь не нужно создавать словарь с данными. Вместо этого нужно
сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через
двоеточие и пробел после ФИО:
Иванов,Иван,Иванович: скалолазание,охота
Петров,Петр,Петрович: горные лыжи
"""

import sys

users = [
    'Иванов,Иван,Иванович\n',
    'Петров,Петр,Петрович\n'
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
difcount = abs(count_hobby - count_users)

if count_hobby < count_users:
    for _ in range(difcount):
        hobby += [None]
elif count_hobby > count_users:
    sys.exit(1)

# print(users, hobby)

with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    for i, n in zip(users, hobby):
        f.write(f'{i}: {n}\n')

with open('users_hobby.txt', 'r', encoding='utf-8') as f:
    users_hobby = f.read()
print(users_hobby)

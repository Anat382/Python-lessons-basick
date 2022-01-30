"""
5. **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.
"""
# решение
# python les_6_task_5.py users.csv hobby.csv users_hobby.txt

import sys


def main(argv):
    """
    write to the file
    :param argv:
    :return:
    """
    program, *args = argv
    args = list(args)

    users = []
    with open(args[0], 'r', encoding='utf-8') as f:
        for i in f:
            users.append(i.replace('\n', ''))

    hobby = []
    with open(args[1], 'r', encoding='utf-8') as f:
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

    with open(args[2], 'w', encoding='utf-8') as f:
        for i, n in zip(users, hobby):
            f.write(f'{i}: {n}\n')

    with open(args[2], 'r', encoding='utf-8') as f:
        users_hobby = f.read()
    print(users_hobby)


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))

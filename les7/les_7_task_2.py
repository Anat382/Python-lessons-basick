"""
2. *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей
структурой:
|--my_project
|--settings
| |--__init__.py
| |--dev.py
| |--prod.py
|   |--mainapp
| |--__init__.py
| |--models.py
| |--views.py
| |--templates
| |--mainapp
| |--base.html
| |--index.html
|--authapp
| |--__init__.py
| |--models.py
| |--views.py
| |--templates
|    |--authapp
| |--base.html
| |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом
текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные
ситуации, библиотеки использовать нельзя.

"""

# !!! Вызов функции  - python les_7_task_2.py E:\test\ config.yaml

import os
import shutil


def create_folder(path):
    """
    create folder
    :param path:
    :return:
    """
    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=True)
        os.mkdir(path)
    else:
        os.mkdir(path)


def main(argv):
    """

    :param argv:
    :return:
    """
    programm, *args = argv
    args = list(args)
    print(args)
    folder = args[0]  # r'E:\Mail_ru geekbrains DATAINGENEER\Основы языка Python\git_lesson\'

    starter = folder + args[-1]  # 'config.yaml'

    print(starter)
    main_dir = folder + 'my_project'

    files = [main_dir
        , main_dir + '\settings'
        , main_dir + '\settings\__init__.py'
        , main_dir + '\settings\_dev.py'
        , main_dir + '\settings\_prod.py'
        , main_dir + '\mainapp'
        , main_dir + '\mainapp\__init__.py'
        , main_dir + '\mainapp\_models.py'
        , main_dir + '\mainapp\_views.py'
        , main_dir + r'\mainapp\templates'
        , main_dir + r'\mainapp\templates\mainapp'
        , main_dir + r'\mainapp\templates\mainapp\base.html'
        , main_dir + r'\mainapp\templates\mainapp\index.html'
        , main_dir + r'\authapp'
        , main_dir + r'\authapp\__init__.py'
        , main_dir + r'\authapp\models.py'
        , main_dir + r'\authapp\views.py'
        , main_dir + r'\authapp\templates'
        , main_dir + r'\authapp\templates\authapp'
        , main_dir + r'\authapp\templates\authapp\base.html'
        , main_dir + r'\authapp\templates\authapp\index.html'
             ]

    with open(starter, 'w', encoding='utf-8') as f:
        for el in files:
            f.write(f'{el}\n')

    with open(starter, 'r', encoding='utf-8') as f:
        for el in f:
            # print(el) if '.html' not in el and '.py' not in el else None
            create_folder(el.replace('\n', '')) if '.html' not in el and '.py' not in el else None

    with open(starter, 'r', encoding='utf-8') as f:
        for el in f:
            open(el.replace('\n', ''), 'w', encoding='utf-8').close() if '.html' in el or '.py' in el else None


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))

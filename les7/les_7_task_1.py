"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
|--settings
|--mainapp
|--adminapp
|--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как
лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить
данные о вложенных папках и файлах (добавлять детали)?

"""

import os
import shutil

def create_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=True)
        os.mkdir(path)
    else:
        os.mkdir(path)


dir_folder = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}

folder = r'E:\Mail_ru geekbrains DATAINGENEER\Основы языка Python\git_lesson\my_project'

create_folder(folder)

for dir_f in dir_folder['my_project']:
    print(os.path.join(folder, dir_f))
    os.mkdir(os.path.join(folder, dir_f))



"""
4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
«Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
Например:
>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "И": {
        "И": ["Илья Иванов"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Как поступить, если потребуется сортировка по ключам?
"""

from collections import defaultdict


def thesaurus_adv(*args):
    """
    convert to dict
    :param args:
    :return:
    """
    args = list(set(args))
    # print(args)
    letter_list = defaultdict(list)
    letter_list_new = defaultdict(list)
    dict_name = {}
    count_ = 0
    for let, elem in dict(zip(args, args)).items():
        args[count_] = (elem[elem.find(' ') + 1:][0:1], (let[0:1], elem))
        count_ += 1
    for let, elem in args:
        letter_list[let].append(elem)
    for i, n in dict(letter_list).items():
        for let, elem in n:
            letter_list_new[let].append(elem)
        dict_name[i] = dict(letter_list_new)
        letter_list_new = defaultdict(list)
    return dict_name


print(dict(sorted(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Илья Иванов",
                                "Анна Петрова", "Анна Савельева", "Анна Hавельева").
                  items(), reverse=False)))
# print(sorted(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Илья Иванов",
#                                 "Анна Петрова", "Анна Савельева", "Анна Hавельева").keys()))

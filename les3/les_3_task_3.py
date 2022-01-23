"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в
 котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
Можно ли использовать словарь в этом случае?
"""

from collections import defaultdict


def thesaurus(*args):
    """
    convert to dict
    :param args:
    :return:
    """
    args = list(set(args))
    # print(args)
    letter_list = defaultdict(list)
    count_ = 0
    for let, elem in dict(zip(args, args)).items():
        args[count_] = (let[0:1], elem)
        count_ += 1
    for let, elem in args:
        letter_list[let].append(elem)
    return dict(letter_list)


print(dict(sorted(thesaurus("Иван", "Мария", "Петр", "Илья").items(), reverse=True)))

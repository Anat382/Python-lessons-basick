
"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, 
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках 
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""

import random as rd


def get_jokes(*args, n=0, **kwargs):
    """
    choice random word
    :param fl: default 0
    :param n: default 0
    :param args: *

    """
    nc = 1
    my_text = []
    text = ''
    while nc <= n:
        for elem in args:
            args_new = list(set(elem)) if kwargs.values() == 1 else elem
            text += rd.choice(args_new) + ' '
        my_text.append(text.strip())
        text = ''
        nc += 1
    return my_text


nouns = ["автомобиль", "лес", "огонь", "огонь", "огонь", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(nouns, adverbs, adjectives, n=3, f=1))

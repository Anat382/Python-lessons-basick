"""
2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
Например:
>>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"

"""

lib_lang = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
            'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(text, dict):
    """
    function trunslate
    :param text:
    :return:
    """
    text_ext = text.lower()
    up_text = text_ext[0:1].upper() + text_ext[1:].lower()
    if up_text == text:
        return dict.get(text_ext, None)[0:1].upper() + dict.get(text_ext, None)[1:].lower()
    else:
        return dict.get(text_ext, None)


print(num_translate('Seven', lib_lang))

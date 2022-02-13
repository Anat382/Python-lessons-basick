"""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного
выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
...
raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
"""

import re

def email_address(email):
    email_adr = {}
    domen = r'(\w+\w+)[@$]'
    domen2 = r'@(\w+\.\w+)'
    try:
        email_adr[re.findall(domen, email)[0]] = re.findall(domen2, email)[0]
    except Exception as exp:
        raise ValueError(f'ValueError: wrong email: {email}')
    return email_adr


test_email = 'someone@geekbrainsru'

print(email_address(test_email))

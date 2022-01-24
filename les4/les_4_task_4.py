"""
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего
задания. Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов
функции currency_rates(). Убедиться, что ничего лишнего не происходит.

"""

import les_4_task_3 as utils


print(utils.currency_rates('USD', 'CHF', 'ru'))
print(utils.currency_rates('UAH', 'US', 'UZS'))
print(utils.currency_rates('BGN', 'SEK', 'NOK'))

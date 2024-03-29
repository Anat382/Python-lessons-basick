"""
3. Создать собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
пользователя данные и заполнять список необходимо только числами. Класс-исключение
должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
пользователь сам не остановит работу скрипта, введя, например, команду «stop». При этом
скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и
строки. Во время ввода пользователем очередного элемента необходимо реализовать
проверку типа элемента. Вносить его в список, только если введено число. Класс-исключение
должен не позволить пользователю ввести текст (не число) и отобразить соответствующее
сообщение. При этом работа скрипта не должна завершаться.
"""


class Check_number(Exception):
    def __init__(self, txt):
        self.txt = txt

    def check(self, number):
        if not number.replace('-', '').isdigit():
            raise Check_number(self.txt)


number_list = []
while True:

    try:
        numer = input("Введите число: ")
        if numer == 'stop':
            break
        Check_number(f"Вы ввели не число: {numer}").check(numer)
        number_list.append(numer)
    except Check_number as exp:
        print(exp)
    else:
        print(number_list)

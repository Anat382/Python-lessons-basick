"""
2. Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class Check_devide(Exception):
    def __init__(self, txt):
        self.txt = txt

    def check(self, denumerator):
        self.__denumerator = denumerator
        if self.__denumerator == 0:
            raise Check_devide(self.txt)


try:
    numer = int(input("Введите чеслитель: "))
    denumer = int(input("Введите знаминатель: "))
    Check_devide("Знаменатель равен нулю").check(denumer)
    res = numer / denumer

except ValueError as exp:
    print(exp.__str__())
except Check_devide as exp:
    print(exp.txt)
else:
    print(res)

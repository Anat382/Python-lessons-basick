"""
3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс «Клетка». В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого
числа деления клеток соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение
количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом
случае метод make_order() вернёт строку: *****\n*****\n**.
Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод
make_order() вернёт строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""

import math


class Cell:
    def __init__(self, cells):
        self.cells = cells
        self.count_cells = self.cells

    def __str__(self):
        return str(self.cells) #f"Кол-во ячеек у клетки ({self.cells})"

    def __add__(self, other):
        print('''Оператор +''')
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        print('''Оператор -''')
        if self.cells - other.cells > 0:
            return Cell(self.cells - other.cells)
        else:
            raise BaseException(f'Чило ячеек клетки меньше чес у основной')

    def __mul__(self, other):
        print('''Оператор *''')
        if self.cells + other.cells > 0:
            return Cell(self.cells * other.cells)
        else:
            raise BaseException('У клетки нет ячеек')

    def __floordiv__(self, other):
        print('''Оператор //''')
        if 0 < self.cells == other.cells > 0:
            return Cell(self.cells // other.cells)
        else:
            raise BaseException('У клеток разное кол-во ячеек')

    def make_order(self, count_val):
        self.count_val = count_val
        # self.count_cells += self.cells
        self.count_cells = Cell(self.cells).cells
        self.rez = []
        for _ in range(math.ceil(self.count_cells / self.count_val)):
            if self.count_cells >= self.count_val:
                self.rez.append('*' * self.count_val + '\n')
            else:
                self.rez.append('*' * abs(self.count_cells) + '\n')

            self.count_cells -= self.count_val
        return ''.join(self.rez)


test_cells = Cell(6)

test_cells2 = Cell(6)
print(test_cells + test_cells2)
# print(test_cells - test_cells2)
print(test_cells * test_cells2)
print(test_cells // test_cells2)
print(test_cells2.make_order(5))

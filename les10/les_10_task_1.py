"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном
виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
"""
import numpy as np
import random


class Matrix:
    def __init__(self, my_array, rows, columns):
        self.my_array = np.array(my_array)
        self.rows = rows
        self.columns = columns
        self.rez_matrix = self.my_array.reshape(self.rows, self.columns)

    def __str__(self):
        return self.rez_matrix

    def __add__(self, other):
        self.new_matrix = Matrix(other.my_array, other.rows, other.columns).rez_matrix
        return np.array(
            [self.rez_matrix[row][column] + self.new_matrix[row][column]
             for row in range(self.rows )
                for column in range(columns)]
        ).reshape(self.rows, self.columns)


rows = 3
columns = 2
size_array = rows * columns

my_array = [random.randint(-100, 100) for _ in range(size_array)]
print("Список 1: \n", my_array)
rez = Matrix(my_array, rows, columns)

my_array = [random.randint(-100, 100) for _ in range(size_array)]
print("Список 2: \n", my_array)
rez2 = Matrix(my_array, rows, columns)

print("Матрица 1: \n", rez.__str__())
print("Матрица 2: \n", rez2.__str__())

print("Сложение матриц: \n", rez + rez2)

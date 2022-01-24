"""
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово
yield, например:
>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration...

"""


def generate_num(n):
    """
   function generate number
   :param n:
   :return:
   """
    for g in range(1, n + 1, 2):
        yield g


num = generate_num(15)
print(*generate_num(15), sep=', ')
print(next(num), next(num), sep=', ')

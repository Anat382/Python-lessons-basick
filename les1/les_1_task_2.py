
"""
2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится
нацело на 7.
* Решить задачу под пунктом b, не создавая новый список.
"""

number_list_ = []


for elem in range(1, 1000):
    num = str(elem ** 3)
    nn = 0
    for n in num:
        nn += int(n)

    if nn % 7 == 0:
        number_list_.append(num)

print('result 1: ', number_list_)


for i in number_list_:
    i_add = i + '17'
    n_res = 0
    for n in i_add:
        n_res += int(n)
    if n_res % 7 != 0:
        number_list_[number_list_.index(i)] = None
    else:
        number_list_[number_list_.index(i)] = i_add

print('result 2: ', list(set(number_list_)))











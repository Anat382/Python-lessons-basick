"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определённое название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке
знания. Реализовать абстрактные классы для основных классов проекта и проверить работу
декоратора @property.
"""


class Costume:
    def __init__(self, growth):
        self.growth = growth

    @property
    def calc_costs(self):
        return 2 * self.growth + 0.3


class Coat:
    def __init__(self, size_):
        self.size_ = size_

    @property
    def calc_costs(self):
        return self.size_ / 6.5 + 0.5


class Clothes:
    select_clothes = []

    def __init__(self, types, param):
        self.types = types
        self.param = param

    @property
    def calc_costs(self):
        if str(self.param).isdigit():
            if self.types == 'Пальто':
                self.__materials_costs = Coat(self.param).calc_costs
                Clothes.select_clothes.append(self.__materials_costs)
            elif self.types == 'Костюм':
                self.__materials_costs = Costume(self.param).calc_costs
                Clothes.select_clothes.append(self.__materials_costs)
            else:
                raise BaseException(f'Типа одежды {self.types} не существует')

            print(f"""Введенные параметры: тип одежды - {self.types}, размер - {self.param}
                , расход ткани - {self.__materials_costs} """)
            return f'Всего расходовано ткани: {sum(Clothes.select_clothes)}'
        else:
            raise BaseException(f'Не верно указан параметр у одежды {self.types}: {self.param}: Введите чило')


prod = Clothes('Пальто', 58)
print(prod.calc_costs)
prod2 = Clothes('Костюм', 180)
print(prod2.calc_costs)

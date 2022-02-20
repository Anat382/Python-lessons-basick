"""
4. Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также
класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведённых типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за
приём оргтехники на склад и передачу в определённое подразделение компании. Для
хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""

from abc import ABC, abstractmethod


class Fail_number(Exception):
    def __init__(self, txt):
        self.txt = txt


class Min_number(Exception):
    def __init__(self, txt):
        self.txt = txt


class Check_number:
    @staticmethod
    def check_number_(number, txt):
        if not isinstance(number, int):
            raise Fail_number(txt)

    @staticmethod
    def check_min(number, txt):
        if number < 0:
            raise Min_number(txt)


class Office_equipment:
    @abstractmethod
    def __init__(self, type, model, color, price, qty):
        self.model = model
        self.type = type
        self.color = color
        self.price = price
        self.qty = qty
        try:
            Check_number.check_number_(self.qty, f"Введено не число !!!!!!!! {self.qty}")
            Check_number.check_min(self.qty, f"Введенное число {self.qty} меньше 0 !!!!!!!")
        except Fail_number as exp:
            print(exp)
            self.qty = 0
        except Min_number as exp:
            print(exp)
            self.qty = 0
        except Exception as exp:
            print(exp)
            self.qty = 0

        self.equipment = [self.type, self.model, self.color, self.price]

    @abstractmethod
    def to_come(self, number):
        return Warehouse(number).to_warehouse(self.equipment, self.qty)

    @abstractmethod
    def to_out(self, number, leftovers):
        return Warehouse(number).out_warehouse(leftovers, self.equipment, self.qty)


class Printer(Office_equipment):
    def __init__(self, type, model, color, price, qty):
        super().__init__(type, model, color, price, qty)

    def to_come(self, number):
        return super().to_come(number)

    def to_out(self, number, leftovers):
        return super().to_out(number, leftovers)


class Scanner(Office_equipment):
    def __init__(self, type, model, color, price, qty):
        super().__init__(type, model, color, price, qty)

    def to_come(self, number):
        return super().to_come(number)

    def to_out(self, number, leftovers):
        return super().to_out(number, leftovers)


class Xerox(Office_equipment):
    def __init__(self, type, model, color, price, qty):
        super().__init__(type, model, color, price, qty)

    def to_come(self, number):
        return super().to_come(number)

    def to_out(self, number, leftovers):
        return super().to_out(number, leftovers)


class Warehouse:
    product_printer = []

    def __init__(self, number):
        self.number_warehouse_ = number

    def to_warehouse(self, nomenclature, qty):
        self.number_warehouse = self.number_warehouse_
        # print(self.number_warehouse)
        self.qty = qty
        # print(self.type, nomenclature)
        self.nomenclature = nomenclature + [self.number_warehouse] + [self.qty]
        self.product_print = Warehouse(self).product_printer

        # print('start', self.product_print)
        if len(self.product_print) > 0:
            # print('chek', self.product_print)
            for i, el in enumerate(self.product_print):
                # print('res ', len(self.product_print), i, el, self.nomenclature, el[:-1] == self.nomenclature[:-1],
                #       el[:-1], list(map(lambda x: x[:-1], self.product_print)))

                if self.nomenclature[:-1] not in list(map(lambda x: x[:-1], self.product_print)):
                    # print('+++', self.product_print[i][-1])
                    self.product_print.append(self.nomenclature)
                    # print('-9--', self.product_print)
                    # print('-' * 200)
                    break
                elif el[:-1] == self.nomenclature[:-1]:
                    self.product_print[i][-1] += self.qty
                    # print('res ++ ', self.product_print)
                    # print('-' * 200)
                    break
        else:
            self.product_print.append(self.nomenclature)
            # print('-10--', self.product_print)
            # print('-' * 200)
        # print(self.product_print)
        return self.product_print

    def out_warehouse(self, leftovers, nomenclature, qty):
        self.number_warehouse = self.number_warehouse_
        # print(self.number_warehouse)
        self.qty = qty
        # print(self.type, nomenclature)
        self.nomenclature = nomenclature + [self.number_warehouse] + [self.qty]
        self.leftovers = leftovers
        # print(self.leftovers, '\n', self.nomenclature, self.qty)

        for i, el in enumerate(self.leftovers):
            if self.nomenclature[:-1] not in list(map(lambda x: x[:-1], self.leftovers)):
                print(f'Номенклатуры {nomenclature[:-1]} не существует!!!')
                break
            elif el[:-1] == self.nomenclature[:-1]:
                if self.qty <= self.leftovers[i][-1]:
                    self.leftovers[i][-1] -= self.qty
                    print(
                        f'Со склада номер {self.number_warehouse}  отгужен товар {self.nomenclature[:-2]},в кол-ве {self.qty} шт., остаток {self.leftovers[i][-1]}')
                else:
                    print(f"""На складе номер {self.number_warehouse} не хватает товара {self.nomenclature[:-2]}, 
                        остатки {self.leftovers[i][-1]} шт., отгрузка {self.qty} шт., 
                        не хватает {abs(self.leftovers[i][-1] - self.qty)} шт. !!!""")

        return self.leftovers


whs = Warehouse(10).number_warehouse_
Printer('Принтер', 'd6868', 'белый', 5000, 10).to_come(whs)
Printer('Принтер', 'sd555', 'белый', 5000, 20).to_come(whs)
Printer('Принтер', 'sd555', 'белый', 5000, 'd').to_come(whs)
Printer('Принтер', 'd6868', 'белый', 5000, 2).to_come(whs)
Printer('Принтер', 'd6868', 'белый', 7000, 17).to_come(whs)
Printer('Принтер', 'sd555', 'белый', 5000, -5).to_come(whs)
# leftovers = Printer('Принтер', 'sd555', 'белый', 5000, 20).to_come(whs)

whs = Warehouse(20).number_warehouse_
Printer('Принтер', 'd6868', 'белый', 5000, 2).to_come(whs)
Printer('Принтер', 'sd555', 'белый', 5000, 20).to_come(whs)
Printer('Принтер', 'd6868', 'белый', 5000, 2).to_come(whs)
Printer('Принтер', 'd6868', 'белый', 7000, 17).to_come(whs)
Printer('Принтер', 'sd555', 'белый', 5000, 5).to_come(whs)
# leftovers = Printer('Принтер', 'sd555', 'белый', 5000, 20).to_come(whs)

whs = Warehouse(20).number_warehouse_
Scanner('Сканер', 'd6868', 'белый', 5000, 2).to_come(whs)
Scanner('Сканер', 'sd555', 'белый', 5000, 20).to_come(whs)
Scanner('Сканер', 'd6868', 'белый', 5000, 2).to_come(whs)
Scanner('Сканер', 'd6868', 'белый', 7000, 17).to_come(whs)
Scanner('Сканер', 'sd555', 'белый', 5000, 5).to_come(whs)
# leftovers = Scanner('Сканер', 'sd555', 'белый', 5000, 20).to_come(whs)

whs = Warehouse(10).number_warehouse_
Xerox('Ксерокс', 'd6868', 'белый', 5000, 2).to_come(whs)
Xerox('Ксерокс', 'sd555', 'белый', 5000, 20).to_come(whs)
Xerox('Ксерокс', 'd6868', 'белый', 5000, 2).to_come(whs)
Xerox('Ксерокс', 'd6868', 'белый', 7000, 17).to_come(whs)
Xerox('Ксерокс', 'sd555', 'белый', 5000, 5).to_come(whs)
leftovers = Xerox('Ксерокс', 'sd555', 'белый', 5000, 20).to_come(whs)

print('\nПриход:', leftovers, sep='\n')
#
print('\nОтгрузка:')
whs = Warehouse(10).number_warehouse_
Printer('Принтер', 'sd555', 'белый', 5000, 10).to_out(whs, leftovers)
Printer('Принтер', 'd6868', 'белый', 5000, 6).to_out(whs, leftovers)
# print('Конечные остататки:',leftovers, sep='\n')

whs = Warehouse(20).number_warehouse_
Printer('Принтер', 'sd555', 'белый', 5000, 10).to_out(whs, leftovers)
Printer('Принтер', 'd6868', 'белый', 5000, 2).to_out(whs, leftovers)
# print('Конечные остататки:', leftovers, sep='\n')

whs = Warehouse(10).number_warehouse_
Scanner('Сканер', 'sd555', 'белый', 5000, 10).to_out(whs, leftovers)
Scanner('Сканер', 'd6868', 'белый', 5000, 2).to_out(whs, leftovers)

whs = Warehouse(20).number_warehouse_
Scanner('Сканер', 'sd555', 'белый', 5000, 10).to_out(whs, leftovers)
Scanner('Сканер', 'd6868', 'белый', 5000, 2).to_out(whs, leftovers)

whs = Warehouse(10).number_warehouse_
Xerox('Ксерокс', 'sd555', 'белый', 5000, 10).to_out(whs, leftovers)
Xerox('Ксерокс', 'sd555', 'белый', 5000, 2).to_out(whs, leftovers)
Xerox('Сканер', '55sa6', 'белый', 5000, 40).to_out(whs, leftovers)
print('\n\nКонечные остататки:', leftovers, sep='\n')

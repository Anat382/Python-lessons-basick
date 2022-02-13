"""
3. Реализовать базовый класс Worker (работник):
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    def __init__(self, name, surname, position, salary, premium):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": salary, "bonus": premium}
        self.salary_prem = self._income


class Position(Worker):
    def __init__(self, name, surname, position, salary, premium):
        super().__init__(name, surname, position, salary, premium)
        self.get_full_name = ' '.join([surname, name])
        self.get_total_income = sum(self.salary_prem.values())

    def __str__(self):
        return 'Сотридник: {}, должность: {}, доход: {} рублей'.format(self.get_full_name, self.position,
                                                                       self.get_total_income)


doc_salary = Position('Иван', 'Иванов', 'Продавец', 50000, 20000)

print(doc_salary.name)
print(doc_salary.surname)
print(doc_salary.position)
print(doc_salary.salary_prem)
print(doc_salary.__str__())

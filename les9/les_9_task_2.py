"""
2. Реализовать класс Road (дорога).
● определить атрибуты: length (длина), width (ширина);
● значения атрибутов должны передаваться при создании экземпляра класса;
● атрибуты сделать защищёнными;
● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
● проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self._width_road = 5

    def total_weight(self):
        self.total_ton = int(self._width * self._length * self.weight * self._width_road / 1000)

    def __str__(self):
        return 'для покрытия всей дороги потребуется {} тонн'.format(self.total_ton)


result = Road(20, 5000)
result.total_weight()
print(result.__str__())

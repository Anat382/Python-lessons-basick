"""
5. Реализовать класс Stationery (канцелярская принадлежность):
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    title = None

    def draw(self):
        print('Запуск отрисовки \n')


class Pen(Stationery):

    def draw(self):
        self.pen = Stationery.title
        print(f'{self.pen} \n Пишем ручкой \n')


class Pencil(Stationery):
    def draw(self):
        self.pencil = Stationery.title
        print(f'{self.pencil} \n Чертим карандашом \n')



class Handle(Stationery):
    def draw(self):
        self.handle = Stationery.title
        print(f'{self.handle} \n Закрашиваем маркером \n')


Stationery = Stationery()
Stationery.draw()

Pen = Pen()
Stationery.title = 'Слово'
Pen.draw()

Pencil = Pencil()
Stationery.title = 'Чертёж'
Pencil.draw()

Handle = Handle()
Stationery.title = 'Озеро'
Handle.draw()



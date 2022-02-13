"""
4. Реализуйте базовый класс Car:
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
"""


class Car:
    speed = None
    color = None
    name = None
    is_police = None

    def __init__(self):
        self.speed = Car.speed
        self.color = Car.color
        self.name = Car.name
        self.is_police = Car.is_police

    def go(self):
        print('поехала')

    def stop(self):
        print('остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'едет {self.direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        # print(self.speed)
        if self.speed > 60:
            print(f'Превышена максимальная скорость движения, движение > 60 запрещёно!!!')


class WorkCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        # print(self.speed)
        if self.speed > 40:
            print(f'Превышена максимальная скорость движения, движение > 40 запрещёно!!!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


Move_car = Car()
Move_car.speed = 50
print(Move_car.speed)
Move_car.name = 'Mazda'
print(Move_car.name)
Move_car.is_police = False
print(Move_car.is_police)
Move_car.color = 'Green'
print(Move_car.color)
Move_car.go()
Move_car.stop()
Move_car.turn('прямо')
Move_car.show_speed()


TownCar = TownCar()
TownCar.show_speed(60)

WorkCar = WorkCar()
WorkCar.show_speed(70)
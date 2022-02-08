"""
1. Создать класс TrafficLight (светофор):
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""

import time


class TrafficLight:
    __color = [None, None, None]
    __count = 0

    def running(self, color):
        TrafficLight.__color[TrafficLight.__count] = color
        color_list = ["красный", "жёлтый", "зелёный"]

        if TrafficLight.__color[0] == color_list[TrafficLight.__count]:
            print(color)
            time.sleep(7)
        elif TrafficLight.__color[1] == color_list[TrafficLight.__count]:
            print(color)
            time.sleep(2)
        elif TrafficLight.__color[2] == color_list[TrafficLight.__count]:
            print(color, '\t\n поехали!!!')
            time.sleep(10)
        else:
            raise BaseException(
                f""" Нарушена последовательность цвета: {TrafficLight.__count + 1} позицией указан {color}, 
                правильная последовательность (красный, жёлтый, зелёный) должен быть: {color_list[TrafficLight.__count]} 
                """)
        TrafficLight.__count += 1


TrafficLight_ = TrafficLight()
TrafficLight_.running('красный')
TrafficLight_.running('жёлтый')
TrafficLight_.running('зелёный')

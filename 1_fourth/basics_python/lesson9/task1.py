"""
Создать класс TrafficLight (светофор).
определить у него один приватный атрибут color (цвет) и метод get_current_signal() (получить текущий цвет);
после создания экземпляра светофора, он запускает режим смены сигналов с разной длительностью: красный (3 сек), жёлтый (1 сек), зелёный (3 сек);
переключение идет циклично в порядке красный-жетлый-зеленый-красный-жетлый-зеленый-красный-...
проверить переключение режимов работы светофора, опрашивая в цикле текущее состояние светофора с интервалом 0.5 секунды, используя метод get_current_signal().
"""

from time import sleep, perf_counter
from itertools import cycle
from datetime import datetime


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']
    time_start = datetime.now()
    
    def get_current_signal(self):
        time_finish = datetime.now()
        delta = (time_finish - self.time_start).total_seconds()
        if delta > 7:
            self.time_start = time_finish
            return self.__color[0]
        elif delta <= 3:
            return self.__color[0]
        elif 3 < delta <= 4:
            return self.__color[1]
        elif 4 < delta <= 7:
            return self.__color[2]
            

a = TrafficLight()
for i in range(100):
    print(a.get_current_signal())
    sleep(0.5)
    

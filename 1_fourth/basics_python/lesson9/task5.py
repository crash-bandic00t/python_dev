"""
Реализуйте базовый класс Car.
при создании класса должны быть переданы атрибуты: color (str), name (str).
реализовать в классе методы: go(speed), stop(), turn(direction), 
которые должны изменять состояние машины - 
для хранения этих свойств вам понадобятся дополнительные атрибуты - придумайте какие.
добавьте метод is_police() - который возвращает True/False, 
в зависимости от того является ли этот автомобиль полицейским (см.дальше)
Сделайте несколько производных классов: TownCar, SportCar, WorkCar, PoliceCar;
Добавьте в базовый класс метод get_status(), который должен возвращать 
в виде строки название, цвет, текущую скорость автомобиля и
направление движения (в случае если автомобиль едет), для полицейских 
автомобилей перед названием автомобиля должно идти слово POLICE;
Для классов TownCar и WorkCar в методе get_status() рядом со 
значением скорости должна выводиться фраза "ПРЕВЫШЕНИЕ!", 
если скорость превышает 60 (TownCar) и 40 (WorkCar).
Создайте по одному экземпляру каждого производного класса. 
В цикле из 10 итераций, для каждого автомобиля сделайте одно из 
случайных действий: go, stop, turn со случайными параметрами. 
После каждого действия показывайте статус автомобиля.
"""
from random import randint


class Car:
    car_status = {
        'speed': 0,
        'turn': None,
    }

    def __init__(self, color, name):
        self.color = color
        self.name = name
    
    def go(self, speed):
        self.car_status["speed"] = speed
    
    def stop(self):
        self.car_status["speed"] = 0
        self.car_status["turn"] = None

    def turn(self, direction):
        self.car_status[turn] = direction

    def get_status(self):
        if self.car_status["speed"] == 0:
            return f'{self.name}, {self.color}, машина не двигается'
        else:
            return f'{self.name}, {self.color}, скорость {self.car_status["speed"]}, направление {self.car_status["turn"]}'

class TownCar(Car):

    speed_limit = 60

class SportCar(Car):

    pass

class WorkCar(Car):

    speed_limit = 40

class PoliceCar(Car):

    def is_police(self):
        return True 

a = TownCar('black', 'Nissan')
b = SportCar('red', 'Ferrari')
c = WorkCar('black', 'UAZ')
d = PoliceCar('black', 'Ford')

# list_of_actions = [b.go(), stop(), turn()]
# list_of_direction = ['left', 'right','straight']

# for i in range(10):
#     b.list_of_actions[randint(0,2)]
#     b.get_status()

print(b.__class__.__name__)
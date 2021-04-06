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
from random import randint, choice


class Car:
    speed_limit = 0
    speed = 0
    turn = 'straight'

    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def __str__(self):
        return f'{self.name} {self.color}'

    def go(self, speed):
        self.speed = speed
    
    def stop(self):
        self.speed = 0
        self.turn = 'straight'

    def turns(self, direction):
        self.turn = direction
    
    def speed_check(self):
        if self.speed_limit != 0:
            if self.speed > self.speed_limit:
                return True
        return False
    
    def get_status(self):
        if self.speed == 0:
            result = f'{self} {self.speed}'
        elif self.speed_check():
            result = f'{self} {self.speed} ПРЕВЫШЕНИЕ! {self.turn}'
        elif not self.speed_check():
            result = f'{self} {self.speed} {self.turn}'
        return result

class TownCar(Car):
    speed_limit = 60

class WorkCar(Car):
    speed_limit = 40

class PoliceCar(Car):
    def __str__(self):
        return f'POLICE {self.name} {self.color}'

class SportCar(Car):
    pass

town = TownCar('Nissan', 'blue')
work = WorkCar('UAZ', 'black')
pol = PoliceCar('Ford', 'white')
sport = SportCar('Ferrari', 'red')

car_list = [town, work, pol, sport]
turn_list = ['straight', 'right', 'left', 'backward']

for i in range(10):
    rand_func = randint(0, 2)
    if rand_func == 0:
        print('Меняем скорость')
        for j in car_list:
            j.go(randint(1,100))
            print(j.get_status())
    if rand_func == 1:
        print('Останавливаемся')
        for j in car_list:
            j.stop()
            print(j.get_status())
    if rand_func == 2:
        print('Поворачиваем')
        for j in car_list:
            j.turns(choice(turn_list))
            print(j.get_status())
    print('-----------')
"""
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw() (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три производных класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе переопределить метод draw(). Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры каждого класса и положить их в список. Проитерироваться по этому списку и вызвать метод draw() для каждого элемента.
"""
class Stationery:
    title = None

    def draw(self):
        return 'Запуск отрисовки'
    
class Pen(Stationery):
    title = 'ручка'

    def draw(self):
        return 'Рисуем ручкой'

class Pencil(Stationery):
    title = 'карандаш'

    def draw(self):
        return 'Рисуем карандашом'

class Handle(Stationery):
    title = 'маркер'

    def draw(self):
        return 'Рисуем маркером'

a = Pen()
b = Pencil()
c = Handle()    
class_list = [a, b, c]
for i in class_list:
    print(i.draw())
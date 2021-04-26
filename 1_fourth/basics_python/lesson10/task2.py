"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Создать абстрактный класс Clothes (одежда). Сделать в этом классе свойство cloth_size
(используя декоратор @property) - размер ткани, необходимый для производства одежды.
Это свойство должно вычислять размерт ткани, вызывая абстрактный метод self.get_size().
Сделать два производных класса одежды: Suit (костюм) и Coat (Пальто).
В конструктор Suit должен принимать параметр height (рост), а Coat - size (размер).
Для определения расхода ткани по каждому типу одежды внутри метода get_size() использовать формулы:

для пальто: (size/6.5 + 0.5)
для костюма: (2*height + 0.3)
Создать список из 10 единиц одежды случайно выбирая один из двух возможных типов со случайным параметром.
Распечатать список одежды: размер требуемой ткани, тип и параметр.
Рассчитать и вывести на экран общий объем ткани, необходимый для пошива всей одежды из этого списка, используя свойство cloth_size. Например:

30.3 - Suit (height: 15)
20 - Coat (size: 3)
13.5 - Coat (size: 2)
4.3 - Suit (seze: 2)
...
Итого: 250.3
"""
from random import randint, choice


class Clothes:
    @property
    def cloth_size(self):
        return self.get_size()

    def get_size(self):
        if self.__class__.__name__ == 'Coat':
            cloth_quantity = f'{format(self.size / 6.5 + 0.5, ".1f")} - {self.__class__.__name__} (size: {self.size})'
        elif self.__class__.__name__ == 'Suit':
            cloth_quantity = f'{format(self.height * 2 + 0.3, ".1f")} - {self.__class__.__name__} (height: {self.height})'
        return cloth_quantity


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

list_of_types = [Coat, Suit]

list_of_cloth = [choice(list_of_types)(randint(30,200)) for i in range(10)]

for i in list_of_cloth:
    print(i.cloth_size)
    
"""
Начните работу над проектом «Склад оргтехники». 
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники
"""
class Sklad:
    rows_cnt = 5            # ряды
    rows_shelf_cnt = 10     # полок в одном ряду

class Equipment:

    def __init__(self, model, position_row, position_shelf):
        self.model = model
        self.position_row = position_row
        self.position_shelf = position_shelf
        

class Printers(Equipment):

    equip_type = 'Принтер'


class Scanners(Equipment):

    equip_type = 'Сканер'
        

class Xerox(Equipment):

    equip_type = 'Ксерокс'


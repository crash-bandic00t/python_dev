"""
Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
"""
class Sklad:
    rows_cnt = 5            # ряды
    rows_shelf_cnt = 10     # полок в одном ряду

class Equipment:

    def __init__(self, model, position_row, position_shelf):
        if self.check_position(position_row, position_shelf):
            self.model = model
            self.position_row = position_row
            self.position_shelf = position_shelf
        else:
            print(f'{self.equip_type} {model} не влезает на склад! Выберите другое место для хранения.')
    
    @staticmethod
    def check_position(position_row, position_shelf):   # проверка есть ли такое место на складе
        if position_row in range(1, Sklad.rows_cnt + 1) and position_shelf in range(1, Sklad.rows_shelf_cnt + 1):
            return True
        else:
            return False
        

class Printers(Equipment):

    equip_type = 'Принтер'


class Scanners(Equipment):

    equip_type = 'Сканер'
        

class Xerox(Equipment):

    equip_type = 'Ксерокс'


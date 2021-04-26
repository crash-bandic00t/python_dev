"""
Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
"""
class Sklad:
    rows_cnt = 5            # ряды
    rows_shelf_cnt = 5      # полок в одном ряду
    storage = {             # хранение информации о кол-ве принтеров и закрепление техники за отделами
        'quantity': {       
            'Printers': 0,
            'Scanners': 0,
            'Xerox': 0
        },
        'department':{      # можно сделать хранение еще и по типу техники в отделах, но в пределах задачи не рационально
            'it': 0,
            'marketing': 0,
            'accounting': 0
        }
    } 
    storage_busy = {        # информация занята ли полка
        1: {
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
        },
        2: {
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
        },
        3: {
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
        },
        4: {
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
        },
        5: {
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
        }
    }    

class Equipment:

    def __init__(self, model, position_row, position_shelf, department):
        if self.check_position(position_row, position_shelf): # проверяем есть ли вообще на скаде такая полка
            self.model = model
            self.position_row = position_row
            self.position_shelf = position_shelf
            self.department = department
            self.add_to_storage(position_row, position_shelf)
        else:
            print(f'{self.equip_type} {model} не влез на склад либо его место занято! Выберите другое место для хранения.')
    
    @staticmethod
    def check_position(position_row, position_shelf):   # проверка есть ли такое место на складе
        if position_row in range(1, Sklad.rows_cnt + 1) and position_shelf in range(1, Sklad.rows_shelf_cnt + 1) and not Sklad.storage_busy[position_row][position_shelf]:
            return True
        else:
            return False

    def add_to_storage(self, position_row, position_shelf): # Добавляем на общий склад и закрепляем за отделом
        Sklad.storage['quantity'][self.__class__.__name__] += 1
        Sklad.storage['department'][self.department] += 1
        Sklad.storage_busy[position_row][position_shelf] = True

        

class Printers(Equipment):

    equip_type = 'Принтер'


class Scanners(Equipment):

    equip_type = 'Сканер'
        

class Xerox(Equipment):

    equip_type = 'Ксерокс'


a = Printers('Brother', 1, 1, 'accounting')
b = Printers('HP', 1, 1, 'it')
c = Scanners('Canon', 2, 4, 'marketing')
d = Scanners('HP', 3, 4, 'accounting')
e = Scanners('Kyocera', 5, 2, 'marketing')
f = Xerox('Xerox', 2, 3, 'accounting')



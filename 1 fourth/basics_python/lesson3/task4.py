# (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     }, 
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"], 
#         "А": ["Анна Савельева"]
#     }
# }
import pprint

def thesaurus_adv(*args):
    dict = {}
    for i in args:
        name_surname = i.split()
        if name_surname[1][0] in dict:
            name = dict[name_surname[1][0]]
            if name_surname[0][0] in name:
                letterName = name[name_surname[0][0]]
                letterName.append(i)
                name.update({name_surname[0][0]: letterName})
            else:
                name.update({name_surname[0][0]: [i]})
        else:
            dict.update({name_surname[1][0]: {name_surname[0][0]: [i]}})
    pprint.pprint(dict)


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Алексей Иванов", "Петр Сазанов", "Игнат Афанасьев", 'Игорь Алферов')
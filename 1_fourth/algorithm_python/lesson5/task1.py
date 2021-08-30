# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

factory = {}
n = int(input('Введите количество предприятий: '))
for i in range(n):                                      # ввод данных о предприятиях
    name = input('Введите название компании: ')
    profit1 = int(input('Прибыль за 1 квартал: '))
    profit2 = int(input('Прибыль за 2 квартал: '))
    profit3 = int(input('Прибыль за 3 квартал: '))
    profit4 = int(input('Прибыль за 4 квартал: '))
    factory[name] = {
        1 : profit1,
        2 : profit2,
        3 : profit3,
        4 : profit4,
        }
# factory = {'кер': {1: 123, 2: 234, 3: 546, 4: 234}, 'цуа': {1: 142, 2: 346, 3: 124, 4: 245}, 'рви': {1: 234, 2: 145, 3: 363, 4: 253}, 'иыр': {1: 634, 2: 252, 3: 361, 4: 347}} # для теста чтобы не вводить вручную
avg = {}                                               
for k,v in factory.items():             
    avg[k] = sum(v.values()) / 4                         # заполнение словаря со средними значениями прибыли за год

avgFactory = sum(avg.values()) / n                       # подсчет средней прибыли между всеми предприятиями   

for k,v in avg.items():                                  # определение, чья прибыль была выше или ниже среднего   
    if v > avgFactory:
        print(f'Прибыль предприятия {k} выше среднего')
    else:
        print(f'Прибыль предприятия {k} ниже среднего')
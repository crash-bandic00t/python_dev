# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех слов, взятых из трёх списков (по одному слову из каждого списка):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import randrange

def get_jokes(count):
    """
    prints the number of jokes that you entered, words in which are randomly selected
    you can choose maximum 5 jokes, because word in jokes never repeat 
    """
    lst = []
    for i in range(count):
        rnd_nouns = randrange(len(nouns))
        rnd_adverbs = randrange(len(adverbs))
        rnd_adjectives = randrange(len(adjectives))
        lst.append(f'{nouns.pop(rnd_nouns)} {adverbs.pop(rnd_adverbs)} {adjectives.pop(rnd_adjectives)}') """Таким образом можно сделать по одному слову в каждой шутке. Можно сделать и с флагом, но это будет дольше. Сделать это можно
        если завести переменную в виде списка куда записывать все выбранные случайно элементы из данного списка слов, а потом сравнивать его с исходным"""
    print(lst)     


get_jokes(3)

print(help(get_jokes))
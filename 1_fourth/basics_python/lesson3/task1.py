# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"

def num_translate(number):
    dictionary = {
        'zero':'ноль',
        'one':'один',
        'two':'два',
        'three':'три',
        'four':'четыре',
        'five':'пять',
        'six':'шесть',
        'seven':'семь',
        'eight':'восемь',
        'nine':'девять',
        'ten':'десять',
    }
    print(dictionary.get(number))

num_translate(input('Введите число на английском языке: \n'))

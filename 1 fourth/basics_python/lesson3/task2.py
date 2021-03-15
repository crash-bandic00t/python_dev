#  * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы. Например:
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(number):
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
    if number[0].isupper():
        print(dictionary.get(number.lower()).title())
    else:
        print(dictionary.get(number))


num_translate_adv(input('Введите число на английском языке: \n'))

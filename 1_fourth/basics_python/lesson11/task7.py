"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""
class ComplexNumber:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        result = self.number + other.number
        return ComplexNumber(result)

    def __mul__(self, other):
        result = self.number * other.number
        return ComplexNumber(result)


a = ComplexNumber(3+2j)
b = ComplexNumber(2+4j)
print((a + b).number)
print((a * b).number)
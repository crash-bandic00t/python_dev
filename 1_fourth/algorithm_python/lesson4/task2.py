# Написать два алгоритма нахождения i-го по счёту простого числа.


# решето Эратосфена
n = int(input("Введите верхнюю границу диапазона: "))
numbers = set(range(2, n+1))                                # заполняем наше множество от 2 до n
simpleNumberList = []
while numbers:                                              # пока множество не пустое, проходит цикл
    simpleNumber = min(numbers)                             # минимальное число в множестве всегда простое
    simpleNumberList.append(simpleNumber)                   # добавляем его в список простых чисел                  
    numbers -= set(range(simpleNumber, n+1, simpleNumber))  # удаляем из множества множество, которое состоит из найденного простого числа и чисел, кратных ему

print(simpleNumberList)


# без решета Эратосфена
n = int(input("n="))
lst=[]
for i in range(2, n+1):
    # пробегаем по списку (lst) простых чисел
    for j in lst:
        if i % j == 0:
            break
    else:
        lst.append(i)
print(lst)

#-- coding: utf-8 --

summ = 0
posled = 0
print('Введте последовательность чисел, последнее 0:')
element = int(input())
while element != 0:
    summ += element
    posled += 1
    element = int(input())
print('Среднее значение суммы последовательности чисел:', summ / posled)
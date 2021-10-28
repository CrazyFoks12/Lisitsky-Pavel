#— coding: utf-8 —

n = int(input('Введите количество чискл Фиббоначчи:'))
summ = 0
(x, y) = (0, 1)
for i in range(1, n):
    (x, y) = (y, x + y)
summ = summ + x
print('Сумма чисел Фиббоначчи:',summ) 
# -- coding: utf-8 --

a=int(input('Введите первое значение '))
b=int(input('Введите второе значение '))
if a<=b:
    for i in range(a,b+1):
        print(i)
else: print('Значение не подходит')
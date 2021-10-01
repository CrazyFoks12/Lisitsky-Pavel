# -- coding: utf-8 --

a = int(input())
b = int(input())
c = int(input())
if a != b:
    if (a * b > c) and (c % a == 0 or c % b == 0):
        print('да')
    else:
        print('нет')
else:
    print('Шоколадка должна быть прямоугольной формы')
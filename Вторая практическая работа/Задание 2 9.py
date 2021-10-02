# -- coding: utf-8 --

def r():
    a = int(input())
    b = int(input())
    c = int(input())
    if a != b:
        if (a * b > c) and (c % a == 0 or c % b == 0):
            return'да'
        else:
            return'нет'
    else:
        return'Шоколадка должна быть прямоугольной формы'
print(r())
# -- coding: utf-8 --

def e():
    a=int(input('Расстаяние между рядами '))
    b=int(input('Расстояние между дорочками в ряду '))
    l=int(input('Длинна кончиков шнурка '))
    N=int(input('Количество дырочек в каждом ряду '))
    print('Ответ ')
    return(2*1+(2*N-1)*a+2*(N-1)*b)
print(e())
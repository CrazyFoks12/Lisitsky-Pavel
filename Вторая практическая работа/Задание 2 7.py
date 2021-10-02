# -- coding: utf-8 --

def Y():
    n = int(input('Введите год '))
    print('Год високосный?')
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
         return 'Да'
    else:
        return 'Нет'
print(Y())
# -- coding: utf-8 --

n = int(input('Введите год '))
print('год високосный?')
if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print('да')
else:
    print('нет')
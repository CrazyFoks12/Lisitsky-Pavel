# -- coding: utf-8 --

print('Введите число ')
n = int(input())
t = n % (60 * 24) // 60
m = n % 60
print(t, ':', m)
#-- coding: utf-8 --

n = int(input('Введите число:'))
a = 2
step = 1
while a <= n:
    a *= 2
    step += 1
print(step - 1)
print(a // 2)
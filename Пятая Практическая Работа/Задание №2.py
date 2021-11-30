#-- coding: utf-8 --

n = int(input('Введите число (не меньшее 2):'))
i = 2
while n % i != 0:
    i += 1
print(i)
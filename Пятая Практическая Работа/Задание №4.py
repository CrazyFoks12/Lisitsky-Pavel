#-- coding: utf-8 --

x = int(input('Введите количество км:'))
y = int(input('Введите количество км в день i:'))
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)
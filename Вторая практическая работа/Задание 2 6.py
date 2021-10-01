# -- coding: utf-8 --

s1 = int(input('Строка 1 '))
sb1 = int(input('Столбец 1 '))
s2 = int(input('Строка 2 '))
sb2 = int(input('Столбец 2 '))
if ((s1 and sb1) >= 1 and (s1 and sb1) <= 8) and ((s2 and sb2) >= 1 and (s2 and sb2) <= 8):
    if (s1 % 2 == 1 and sb1 % 2 == 1) or (s1 % 2 == 0 and sb1 % 2 == 0) :
        c1 = str("Белый")
    else:
        c1 = str("Черный")
    if (s2 % 2 == 1 and sb2 % 2 == 1) or (s2 % 2 == 0 and sb2 % 2 == 0):
        c2 = str("Белый")
    else:
        c2 = str("Черный")
else:
    print("Ошибка")
print("Цвета совпадают?")
if c1 == c2:
    print("Да")
else:
    print("Нет")
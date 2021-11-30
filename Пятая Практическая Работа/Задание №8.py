#-- coding: utf-8 --

print('Ряд чисел:')
a = -1
b = 0
b = 0
c = int(input())
while c != 0:
    if a == c:
        b += 1
    else:
        a = c
        b = max(b, b)
        b = 1
    c = int(input())
b= max(b, b)
print('Ответ: ', b)
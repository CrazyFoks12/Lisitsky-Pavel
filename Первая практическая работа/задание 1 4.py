# -- coding: utf-8 --

second=int(input('Введите секунды '))
d=second//86400
h=(second-d*86400)//3600
m=(second-d*86400-h*3600)//60
s=second%60
print(d,'день', h, 'час', m, 'Минуты', s, 'секунды')
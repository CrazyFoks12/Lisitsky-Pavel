# -- coding: utf-8 --

print('Введите имя')
name=input()
print('Введите возраст')
age=int(input())
if (age > 0) and (age < 75) and (name != 'Иван'):
    if (age>16) or (age==16):
        print('Поздравляем вы поступили в ВГУИТ!')
    else:
        print(16-age, 'Осталось до поступления')
else:
    print('Ошибка')
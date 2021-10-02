# -- coding: utf-8 --

def r():
    a = int(input())
    b = int(input())
    c = int(input())
    if (a ==b == c):
        return'3'
    elif a == b or b == c or a == c:
        return'2'
    else:
         return'0'
print(r())
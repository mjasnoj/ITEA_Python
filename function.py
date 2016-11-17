# coding=utf-8

print abs(-2)

print pow(2,3)

print min(1,2,3,4,5)

a, b = divmod(5, 2)

print a
print b

"""
1. Функция должна занимать не более одного Экрана
2. Не более 3 уровней вложенности
3. Название должно начинаться с глагола
"""

def f():
    pass

def add(x, y):
    return x + y

print add(2, 3)
print add('a', 'b')
print add(['a'], ['b'])


"""
SyntaxError не ловится с помощью try
"""

""" позиционные параметры """
def mul(a, b=2):
    return a * b

print mul(3)
print mul(3, 4)


""" именованные параметры"""

def f(a=1,b=2,c=3):
    return a+b+c

print f()
print f(a=2)
print f(a=3,b=2,c=1)

""" fail: print f(c=3, 2) """

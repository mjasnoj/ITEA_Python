# coding=utf-8

t = (1,2,3)
print t

t = 1,2,3
print t

t = 1,
print t

tt = 1.
print tt

#t[0] = 32
"""
Кортежи работают быстрее чем списки
можно конвертировать списки в кортежи и использовать как ключи в словаре
"""

d = {}

d[1,2,3] = 2
d[4,5,6] = 2
d[7,8,9] = 2

print d

l = []
l = d.keys()
l.sort()
print l


a, b, c = 1, 2, 3
a, b = b, a

def addmul(x ,y):
    return x + y, x * y

a, b = addmul(2, 3)
print a, b

fields = ('id', 'name', 'age')
values = (123, 'Bob', 40)
print dict(zip(fields, values))

ID, NAME, AGE = 0, 1, 2
print values[ID]

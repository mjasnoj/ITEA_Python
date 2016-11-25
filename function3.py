# coding=utf-8

print min(1,2)
print min(1,2,3,4)


def f(*args, **kwargs):                # args kwargs are not registered as variables for functions. You can use any other name.
    print args, kwargs

f(1,2,3,4,5,b=32, c=45)                # args - tuple, kwargs - dictionary
                                       # keyword arg should be before non-keyword

f()


def f(a, *args):
    print a, args                       # a parametr is obligatory


def sum_(*args):
    s = 0
    for i in args:
        s += i
    return s


print sum_(1,2,3,4,5,6)
print sum_()


def sum_(a, *args):
    for i in args:
        a += i
    return a


print sum_(1,2,3,4,5,6)
#print sum_()                           # Error


def f(a, b, c):
    print a + b + c

t = 1, 2, 3

f(*t)
f(*[1, 2, 3])

d = {'a' : 2, 'b' : 4, 'c' : 5}
f(**d)

def f():
    def g(x):                       # Each time we call f() new g() function is created
        return 2 * x
    return g

double = f()

print type(double)

print double(4)

print f()(5)

a = 3

def f():
    def g(x):
        return a * x
    return g

my_g = f()

print my_g(3)
a = 5

print my_g(3)


def f():
    b = a                           # Лексическое замыкание. Ссылка на объект сохраняется внутри функции.
    def g(x):
        return b * x
    return g

my_g = f()

print my_g(2)                       # 2 * 5 = 10

a = 7

print my_g(2)                       # 2 * 5 = 10, but not 2 * 7 = 14

def mul(x):
    def g(y):
        return y * x
    return g

double = mul(2)
print double(2)

triple = mul(3)
print triple(2)

l = []
for i in range(10):
    def f(x, a=i):
        return a * x
    l.append(f)

print l                         # all functions use such i value that they got during creation
print i

print l[0](1)
print l[1](1)
print l[5](1)


print l[5](1, 5)
print l[4](1, 5)





def mul(a, x):
    return a * x

import functools

double = functools.partial(mul, 2)      # result function will have only one parametr

print double(5)                         # 10

import operator

double = functools.partial(operator.mul, 2)
print double(6)                         # 12

inc = functools.partial(operator.add, 1)
print inc(6)                            # 7





def composition(f, g):
    return lambda x: f(g(x))

quadruple = composition(double, double)
print quadruple(5)

def odd(x):
    return x % 2

even = composition(operator.not_, odd)
print even(2)
print even(3)


even = composition(odd, functools.partial(operator.add, 1))
print even(2)
print even(3)


def f(x):
    if type(x) == int:
        print "Int"
    elif type(x) == str:
        print "Str"
    else:
        print "Smth"

f(1)
f('aa')
f(True)

print isinstance(1, int)
print isinstance(1, (int, float))

l = [(1,2), (2,3), (2,1), (3,7), (1,5), (3,2)]
l.sort()                    # by first value then by second one
print l

l.sort(key=lambda x: x[1])
print l


import random
random.shuffle(l)
print l

l.sort(key=lambda x: x[0] + x[1])
print l

l.sort(key=operator.itemgetter(1))
print l


l = ['1', '2','3','11','21']
l.sort()
print l

l.sort(key=int)
print l


print sorted(l)         # sorted creates new list instead of modifying old one

print sorted(l, key=int)

print list(reversed(l))

a = reversed(l)

print a.next()
print a.next()
print a.next()
print a.next()
print a.next() 

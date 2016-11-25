# coding = utf-8

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

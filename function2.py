# coding=utf-8

def f(x):
    return 2 * x

def s(a=1, b=2, c=3):
    return a + b + c

s()
s(3,4) # defined only a and b позиционные параметры

s(b=3) # именованные параметры

# s(c=3, 3) # сначала позиционные, потом именованные, а не наоборот, иначе синтаксическая ошибка

def f(a, l=[]):
    l.append(a)
    print l

f(2, [1, 2, 3])
f(1)
f(1)
f(2)

def f(x):
    return 2 * x

double = f # double became a function
double1 = f(0) # function execution

print double(4)

del f # double function stil exists

def execute(f, x): # gets function and variable
    return f(x)

print execute(double, 2)

def f():
    def g(x):
        return 2 * x
    return g

double = f() # double became g function
print double(5)

a = 5
print a # all such variables are stored in globals() dictionary

print globals()

print dir(__builtins__)

def f():
    b = 7
    print locals() # exists only inside functions

f()

a = 1
def f():
    a = 2
    def g():
        a = 3
        print a # LEGB - Local Enclosed Global Builtin
    g()
f()

def f():
    print a
    a = 2

# f() # Error = UnboundLocalError: local variable 'a' referenced before assignment
# a variable exists but not initialized yet
# local dictionary is created after function call
a = 1
def f():
    a = 2 # local variable

def f():
    global a
    a = 2 # global variable . Bad practice to use. Only for tests or debug.

def f():
    b = a
    print b

# a > 1 or f()  - short algoritm is used and f() will not be called

# in Python 3 added "non local" keyword

print map(double, [1,2,3,4,5,6]) # executes function for each element of list. Allows to avoid loops and recursion

def odd(x):
    return x % 2

print odd(3)

print filter(odd, [1,2,3,4,5]) # return list of values that returns true result

print [2 * x for x in [1,2,3,4,5,6] if x % 2] # this function is much more fast than map function because it's just C# code

def add(x, y):
    return x + y

print reduce(add, [1,2,3,4,5,6])
print reduce(add, ["a", "b", "c"])

print map(lambda x: 2 * x, [1,2,3,4,5])  # lambda - anonimus function that will be destroyed after map execution. lambda should be not longer than 1 row

double = lambda x: 2 * x # such way is not recomended. use def.

#help(abs)

def add(x, y):
    """
    Add x and y"""
    return x + y

help(add)

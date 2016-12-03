# coding: utf-8

def a(x):
    print "Func a"

def b(x):
    print "Func b"

def c(x):
    print "Func c"

"""
observers = []

def f():
    print "Do things"
    for o in observers:
        o()

f()

observers.append(a)

f()

observers.append(b)

f()


print "-"*40
"""

class Observers(object):
    def __init__(self):
        self.observers = []
    def add(self, o):
        self.observers.append(o)
    def delo(self, o):
        self.observers.remove(o)
    def observe(self, f):
        def wrapper():
            r = f()
            for o in self.observers:
                o(r)
            return r
        return wrapper

obs = Observers()

@obs.observe
def f():
    print "Do smth"

f()

print "-"*40

obs.add(a)

f()

print "-"*40

obs.add(c)

f()

print "-"*40

obs.delo(c)

f()


"""
Do smth
----------------------------------------
Do smth
Func a
----------------------------------------
Do smth
Func a
Func c
----------------------------------------
Do smth
Func a
"""

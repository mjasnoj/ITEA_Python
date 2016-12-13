# class ClassName(object):
#    """docstring for ."""
#    def __init__(self, arg):
#        super(, self).__init__()
#        self.arg = arg

class Table(object):
    def __init__(self, l, w, h):
        print "Init"
        self.l = l
        self.w = w
        self.h = h

t1 = Table(100, 50, 60)
t2 = Table(110, 40, 55)

print vars(t1)
print vars(t2)


class A(object):
    def f(self):
        print "Class A"

class B(object):
    def f(self):
        print "Class B"

a = A()
a.f()

print "-"*50

print a.__class__               # variable with class name
a.__class__ = B

print a.__class__

a.f()

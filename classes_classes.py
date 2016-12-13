class A(object):
    pass

a = A()
print a

a.x = 1

print vars(a)

a.y = 2

print vars(a)

del a.x

print vars(a)

print a.__dict__

b = A()

print b.__dict__

######### independent instances of A class

b.y = 2

print a == b            # different spaces


print "-"*50

class B(object):
    def set_x(self, x):              # self obligatory parametr - link to instance
        print self
        self.x = x

b = B()
print b
b.set_x(3)

print b.x

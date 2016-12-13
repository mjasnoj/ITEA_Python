class A(object):
    a = 1

a = A()
print a.a

a.a = 2
print a.a

print A.a

b = A()

print b.a

A.a = 5

print a.a , b.a



class C(object):
    counter = 0
    def __init__(self):
        C.counter += 1

a = C()
b = C()
c = C()

print C.counter

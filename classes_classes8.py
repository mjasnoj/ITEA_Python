#coding=utf-8

class A(object):
    def __init__(self):
        print "A"
        super(A, self).__init__()

class B(A):
    def __init__(self, *args, **kwargs):
        print "B"
#        super(B, self).__init__()


class C(A):
    def __init__(self, *args, **kwargs):
        print "C"
        super(C, self).__init__(*args, **kwargs)

class D(B):
    def __init__(self):
        print "D"
        super(D, self).__init__()

class E(B):
    def __init__(self):
        print "E"
        super(E, self).__init__()

class F(C):
    def __init__(self):
        print "F"
        super(F, self).__init__()

class G(E, F):
    def __init__(self):
        print "G"
        super(G, self).__init__()

class H(D, G):
    def __init__(self):
        print "H"
        super(H, self).__init__()


"""
>>> from classes_classes8 import *
>>> h = H()
H
D
G
E
B
F
C
A
>>>

порядок вызова супера зависит от того, где в иерархии находится класс
"""


"""
>>> from classes_classes8 import *
>>> H()
H
D
G
E
B
<classes_classes8.H object at 0x7f38c8de0390>


если есть супер в иерархии хоть где-то, то он должен быть везде
"""

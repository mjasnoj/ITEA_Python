#coding=utf-8

class A(object): pass

class B(A): pass

class C(A): pass

class D(B): pass

class E(B): pass

class F(C): pass

class G(E, F): pass

class H(D, G): pass


"""
>>> from classse_classes5 import *
>>>
>>>
>>> H.mro()
[<class 'classse_classes5.H'>, <class 'classse_classes5.D'>, <class 'classse_classes5.G'>, <class 'classse_classes5.E'>, <class 'classse_classes5.B'>, <class 'classse_classes5.F'>, <class 'classse_classes5.C'>, <class 'classse_classes5.A'>, <type 'object'>]
>>>
"""

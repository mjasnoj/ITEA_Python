# coding: utf-8

>>> class A(object):
...     def __init__(self, n):
...             self.n = n
...     def __call__(self, x):
...             return self.n * x
...
>>> double = A(2)
>>> double(4)
8
>>> triple = A(3)
>>> triple(2)
6



Аналог замыкания

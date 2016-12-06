# coding: utf-8
"""
класс наследуется от класса, класс наследуется от обджект, метакласс наследуется от обджект, метакласс создает класс
type - конструктор класса, метакласс


>>> A = type('A', (object,), {})            А - экземпляр класса type
>>> class A(object):
...     pass


>>> A = type('A', (object,), {'a':1})
>>> a = A()
>>> a.a
1

"""

class Meta(type):
    def __new__(cls, name, parents, attrs):
        new_attrs = {name : value
            for name, value in attrs.items() if not name.startswith('unused')}
        return type.__new__(cls, name, parents, new_attrs)

class A(object):
    __metaclass__ = Meta
    a = 1
    unused_a = 1

print A.a
#print A.unused_a           error


print "-"*40

import abc

class BaseClass(object):
    __metaclass__ = abc.ABCMeta
    def f(self):
        print ('Base.f')
    @abc.abstractmethod
    def g(self):
        pass

#b = BaseClass()
#TypeError: Can't instantiate abstract class BaseClass with abstract methods g

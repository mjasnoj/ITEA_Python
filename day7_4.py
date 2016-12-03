>>> class A(object):
...     def __new__(cls, *args, **kwargs):
...             print "New"
...             return super(A, cls).__new__(cls, *args, **kwargs)
...     def __init__(self):
...             print "init"
...
>>> a =A()
New
init



class A(object):
    def __new__(cls):
        return 42

>>> class A(object):
...     def __new__(cls):
...         return 42
...
>>>
>>> a = A()
>>> a
42




class Singletone(object):
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

"""
>>> s1 = Singletone()
>>> s = Singletone()
>>>
>>>
>>> s is s1
True
>>> s._instance
<__main__.Singletone object at 0x7f5017bc6450>
>>> s1._instance
<__main__.Singletone object at 0x7f5017bc6450>

не работает в многопоточной среде
"""

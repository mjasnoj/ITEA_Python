class A(object):
    def __init__(self):
        self.a = 0              # public variable
        self._donttouchme = 0   # could be changed but could lead to fail (starts with _ )
        self.__secret = 0       # privat variable (starts with __ )


a = A()
print a.a
print a._donttouchme
# print a.__secret              # returns error AttributeError: 'A' object has no attribute '__secret'

print vars(a)



class AA(object):
    __a = 0

class BB(AA):
    __a = 1

b = BB()



class AAA(object):
    def f(self):
        print "f"
    @classmethod
    def g(cls):                     # class method
        print "g"
    @classmethod
    def h(cls):                     # class method
        print "h"

a = AAA()

a.f()
a.g()
a.h()

AAA.g()
AAA.h()
# AAA.f()  # returns error



class BBB(object):
    @staticmethod
    def f():                        # не привязан ни к чему. вызывается без селф
        print "f"
    @classmethod
    def g(cls):                     # class method. Имеет досутп к переменным класса из которого вызывается
        print cls.a


class CCC(BBB):
    a = 2

b = CCC()

b.f()
b.g()


"""
>>> class A(object):
...     instances = []
...     def __init__(self):
...             self.__class__.instances.append(self)
...     @classmethod
...     def get_inst(cls):
...             return cls.instances
...
>>> A()
<__main__.A object at 0x7fcee6bce090>
>>> A()
<__main__.A object at 0x7fcee6bce110>
>>> A.get_inst()
[<__main__.A object at 0x7fcee6bce090>, <__main__.A object at 0x7fcee6bce110>]

"""

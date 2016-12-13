class ReprMixin(object):
  def __repr__(self):
    return '{}({})'.format(
      self.__class__.__name__,
      ', '.join(['{}={}'.format(k, v) for k, v in self.__dict__.items()])
    )

class EqMixin(object):
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        """ # to allow comparison only if $other is Person """
        return self.__dict__ == other.__dict__

class Person(ReprMixin, EqMixin):
    def __init__(self, name, age):
        self.name, self.age = name, age
        self.f = lambda x: 42
    def __getstate__(self):
        return{
            'name': self.name,
            'age': self.age
        }
    def __setstate__(self, obj):
        self.__init__(**obj)
#    def __hash__(self):
#        return hash(self.name)
#    def __eq__(self, other):
#        return self.name == other.name



"""
>>> Person('John', 10)
Person(age=10, name=John)
>>> Person('John', 10) == Person('John', 10)
True


>>> class A(object):
...     pass
...
>>> a = A()
>>> a.name = 'John'
>>> a.age = 10
>>> Person('John', 10) == a
True


After update

>>> p = Person('Bill', 43)
>>> p == 1
False
>>> p == Person('Bill', 43)
True




>>> class Person(ReprMixin, EqMixin):
...     def __init__(self, name, age):
...         self.name, self.age = name, age
...     def __hash__(self):
...         return hash(self.name)
...     def __eq__(self, other):
...         return self.name == other.name
...
>>> {Person('bill', 22), Person('bob', 32), Person('bill', 32)}
set([Person(age=32, name=bob), Person(age=32, name=bill)])

"""



"""
>>> p = Person('Bill', 23)
>>> [p
...
KeyboardInterrupt
>>> p
Person(age=23, name=Bill)
>>> d = {p: 1}
>>> d[p]
1
>>> p.name = 'John'
>>> d
{Person(age=23, name=John): 1}
>>> d[p]
1
>>> d[Person('John', 23)
... ]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: Person(age=23, name=John)
>>> d[Person('John', 23)]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: Person(age=23, name=John)

нельзя использовать мьютебл объекты как

"""

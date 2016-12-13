import numbers

class ReprMixin(object):
  def __repr__(self):
    return '{}({})'.format(
      self.__class__.__name__,
      ', '.join(['{}={}'.format(k, v) for k, v in self.__dict__.items()])
    )

class Number(ReprMixin):
    def __init__(self, value):
        self.value = value
    def __add__(self,other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        elif isinstance(other, numbers.Number):
            print 1
            return Number(self.value + other)
        else:
            return NotImplemented
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        print "iadd"
        return self.__


"""
>>> n = Number(5)
>>> n
Number(value=5)
>>>
>>>
>>>
>>> class Number(ReprMixin):
...     def __init__(self, value):
...         self.value = value
...     def __add__(self,other):
...         return Number(self.value + other.value)
...
>>> Number(4) + Number(3) + Number(2)
Number(value=9)

>>> Number(5) + 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in __add__
AttributeError: 'int' object has no attribute 'value'





>>> class Number(ReprMixin):
...     def __init__(self, value):
...         self.value = value
...     def __add__(self,other):
...         if isinstance(other, Number):
...             return Number(self.value + other.value)
...         elif isinstance(other, numbers.Number):
...             print 1
...             return Number(self.value + other)
...         else:
...             return NotImplemented
...
>>> Number(2) + 3
1
Number(value=5)


>>> a = 4
>>> Number(2) + a
1
Number(value=6)
>>> Number(2) + 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'Number' and 'str'
>>> 3 + Number(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'Number'




>>> Number(10) + 10
1
Number(value=20)
>>> 10 + Number(10)
1
Number(value=20)
>>> 10 + Number(10)



>>> 1 == Number(1)
False
>>> a = Number(4)
>>> a += 5
1
>>> a
Number(value=9)




"""

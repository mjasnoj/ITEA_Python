class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return "Person({}, {})".format(self.name, self.age)
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    def __lt__(self, other):
        return self.age < other.age


p1 = Person('Bill', 23)
p2 = Person('Phill', 23)
p3 = Person('Bill', 23)


print p1 == p3          # because of __eq__
print id(p1)
print id(p3)

l = [Person('Aphill2', 25), Person('Bill1', 22), Person('Bill3', 23)]
print l.index(Person('Bill1', 22))

l.sort()    ## will be sorted by age because of __lt__

print l

print Person('Aphill2', 25) < Person('Aphill2', 32)         # norm
print Person('Aphill2', 45) > Person('Aphill2', 32)         # not correct. __gt__ should be initialized. @total_ordering from functools creates all functions from lt and gt







"""

>>> def scale(f):
...     def wrapper(x):
...             return f(2*x)
...     return wrapper
...
>>> @scale
... def double(x):
...     """Double x"""
...     return 2*x
...
>>> double
<function wrapper at 0x7f1414add6e0>
>>> double.__name__
'wrapper'


>>> def scale(f):
        @functools.wrap
...     def wrapper(x):
...             return f(2*x)
...     return wrapper
...
>>> @scale
... def double(x):
...     return 2*x
...     """Double x"""
...
>>> double
<function wrapper at 0x7f1414add6e0>
>>> double.__name__
'wrapper'

"""

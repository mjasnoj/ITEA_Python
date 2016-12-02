class ReprMixin(object):
  def __repr__(self):
    return '{}({})'.format(
      self.__class__.__name__,
      ', '.join(['{}={}'.format(k, v) for k, v in self.__dict__.items()])
    )

class EqMixin(object):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class ClassName(ReprMixin, EqMixin):
    def __init__(self, name, age):
        self.name, self.age = name, age


"""
>>> ClassName('John', 10)
ClassName(age=10, name=John)
>>> ClassName('John', 10) == ClassName('John', 10)
True


>>> class A(object):
...     pass
...
>>> a = A()
>>> a.name = 'John'
>>> a.age = 10
>>> ClassName('John', 10) == a
True



"""

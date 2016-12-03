# coding: utf-8

"""
>>> def f():
...     for i in range(5):
...             yield i
...             print "I'm here"
...
>>> f()
<generator object f at 0x7f88fb0a9f50>
>>> dir(f())
['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'gi_code', 'gi_frame', 'gi_running', 'next', 'send', 'throw']
>>> g = f()
>>> g.next()
0
>>> g.next()
I'm here
1
>>> g.next()
I'm here
2
>>> g.next()
I'm here
3
>>> g.next()
I'm here
4
>>> g.next()
I'm here
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
"""

class MyList(object):
    def __init__(self, l=[]):
        self._l = l[:]
    def __repr__(self):
        return repr(self._l)
    def __len__(self):
        return len(self._l)
    def __contains__(self, value):
        return value in self._l
    def add(self, value):
        self._l.append(value)
    def __setitem__(self, index, value):
        self._l[index] = value
    def __getitem__(self, index):
        if isinstance(index, int):
            return self._l[index]
        elif isinstance(index, tuple):
            return [self._l[x] for x in index if 0 <= x < len(self._l)]
        elif index == Ellipsis:
            return self._l[:]
        #print index
        #return self._l[index]
    def __iter__(self):
        for i in self._l:
            yield i


"""
>>> l = MyList([1, 2, 3, 4, 5])
>>> for i in l:
...     print i
...
1
2
3
4
5
>>> for i in l:
...     for j in l:
...             print i,j
...
1 1
1 2
1 3
1 4
1 5
2 1
2 2
2 3
2 4
2 5
3 1
3 2
3 3
3 4
3 5
4 1
4 2
4 3
4 4
4 5
5 1
5 2
5 3
5 4
5 5
"""


"""
>>> class MyList(list):
...     def sum(self):
...             s = 0
...             for i in self:
...                     s += 1
...             return s
...
>>> l = MyList([1,2,3])
>>> l[0]
1
>>> len(l)
3
>>> l.sum()
3
"""


class MyList(object):
    def __init__(self, l):
        self._l = l
    def __repr__(self):
        return repr(self._l)

"""
>>> l = MyList([1,2,3,4])
>>> l
[1, 2, 3, 4]
>>> l1 = [1,2,3,4]
>>> l = MyList(l1)
>>> l
[1, 2, 3, 4]
>>> l1[0]
1
>>> l
[1, 2, 3, 4]
>>> l1[0] = 0
>>> l
[0, 2, 3, 4]

"""


class MyList(object):
    def __init__(self, l=[]):
        self._l = l[:]
    def __repr__(self):
        return repr(self._l)

"""
>>> l = MyList(l1)
>>> l
[0, 2, 3, 4]
>>> l1[0] = 32
>>> l1
[32, 2, 3, 4]
>>> l
[0, 2, 3, 4]

"""

class MyList(object):
    def __init__(self, l=[]):
        self._l = l[:]
    def __repr__(self):
        return repr(self._l)
    def __len__(self):
        return len(self._l)

"""
>>> l = MyList(l1)
>>> len(l)
4
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
        return self._l[index]

"""
>>> l = MyList(l1)
>>> l
[32, 2, 3, 4]
>>> l[0]
32
>>> l[0] = 23
>>> l
[23, 2, 3, 4]
>>> 2 in l
True
>>> 1 in l
False

>>> l[7] = 156
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 13, in __setitem__
IndexError: list assignment index out of range


>>> l.add(32)
>>> l
[23, 2, 3, 4, 32]

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



"""
>>> l = MyList(l1)
>>> l
[32, 2, 3, 4]
>>>
>>>
>>>
>>> l = MyList()
>>> l
[]
>>> l[4]
4
>>> l[4,3,5]
(4, 3, 5)
>>> l[2:5]
slice(2, 5, None)
>>> l[2:3, 3, 4:5]
(slice(2, 3, None), 3, slice(4, 5, None))
>>> l[...]
Ellipsis
"""


"""
>>> l = MyList([1,2,3,4,5])
>>> l
[1, 2, 3, 4, 5]
>>> l[0,2,4,10]
[1, 3, 5]
>>> l[...]
[1, 2, 3, 4, 5]
>>> for i in l:
...     print i
...
1
2
3
4
5
Старый протокол итератора - вызов __getitem__ пока не получится ИндексЕррор
Старый протокол криво работает со словарями

Новый протокол работает с двусмя методами:
__iter__
next
в конце - СтопИтерейшн
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
        print "Iter"
        #return iter(self._l)
        self.i = 0
        return self
    def next(self):
        print "Next"
        if self.i == len(self._l):
            raise StopIteration
        self.i += 1
        return self._l[self.i - 1]
"""
>>> for i in MyList([1,2,3]):
...     print i
...
Iter
1
2
3


>>> l = MyList([1,2,3])
>>> for i in l:
...     for j in l:
...             print i, j
...
Iter
Next
Iter
Next
1 1
Next
1 2
Next
1 3
Next
Next

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
        return MyListIterator(self._l)

class MyListIterator(object):
    def __init__(self, l):
        self._l = l
        self.i = 0
    def __iter__(self):
        return self
    def next(self):
        print "Next"
        if self.i == len(self._l):
            raise StopIteration
        self.i += 1
        return self._l[self.i - 1]

"""
>>> l = MyList([1,2,3])
>>> for i in l:
...     for j in l:
...             print i, j
...
Next
Next
1 1
Next
1 2
Next
1 3
Next
Next
Next
2 1
Next
2 2
Next
2 3
Next
Next
Next
3 1
Next
3 2
Next
3 3
Next
Next
"""

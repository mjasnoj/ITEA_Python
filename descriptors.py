# coding: utf-8
class Length(object):
    def __get__(self, obj, objtype):
        return obj._l * 10
    def __set__(self, obj, value):
        obj._l = value / 10

class Line(object):
    l = Length()
    def __init__(self):
        self._l = 0

l = Line()
print l.l
l.l = 100
print l._l
print l.l

print "-"*40
print "-"*40
print "-"*40

class Line(object):
    def __init__(self):
        self._l = 0
    @property
    def l(self):
        return self._l * 10
    @l.setter
    def l(self, value):
        self._l = value / 10

l = Line()
print l.l
l._l = 10
print l._l
print l.l
l.l = 20
print l._l
print l.l

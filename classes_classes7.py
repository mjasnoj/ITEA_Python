#coding=utf-8

class Point(object):
    __slots__ = ('x', 'y', 'z')
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

p = Point(1, 2, 3)

print p.x

p.a = 5         # a var could not be initialized

print p.a       # returns error trying to print a


"""
slots is used for for memory optimization: classes with slots don't have __dict__ and just have __slots__
ReporMixin will not work for Point class
"""

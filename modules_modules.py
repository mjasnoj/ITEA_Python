# coding=utf-8

# any *.py file with Python code is module

import module1
import sys

a = 3

print sys.modules['module1'].a          # a variable is not copied to our namespace
print module1.a
print a


from module1 import a                   # a variable is copied to our namespace

print a

import module1

reload(module1)                         # only for debug in console

m = __import__('module1')               # gets module name as string - usefull for load module listed in config file

serializer = __import__('json')

print serializer.dumps([1, 2, 3])

serializer = __import__('pickle')

print serializer.dumps([1, 2, 3, 4])

a = 5
module1.f()                             # module functions depend on variables declared in module


import package
import package.m1

# coding=utf-8
a = 'hello'
b = 'football'

print b[0]

print len('football')

print 'foot' + 'ball'

print 'A' * 20

print [1] * 10

l = [[1]*3 for i in range(3)]
print l

a = 1 if 1==0 else 2

print [x for x in range(5)]
print [2*x for x in range(5)]

import random

print [random.randint(1,5) for x in range(5)]
print [2*x for x in range(5) if x % 2]

print [[x, y] for x in [1,2,3] for y in [4,5,6]]

print "123".isdigit()

print "abrakadabra".replace("ab","ba")

print "  sdfsd  efas asdfs ".strip()
print "assdf123".isalpha()
print "assdf".isalpha()

print "dsdfgsdfgdf, svdf dfsdf vdf.dsvsdfvf".translate(None, ',.')

print "aaaaaa".find('b')
print "aaaaaa".find('a')

print "file.py".endswith('.py')

print ' 5'.zfill(5)

print "Title".center(40)

print '1,2,3,4,5'.split(',')
""" Если не указан разделитель - по пробелу"""

l = '1,2,3,4,5'.split(',')
print ' '.join(l)

s = ''
for i in range(32, 127):
    s += chr(i)

print s

print [chr(i) for i in range(32, 127)]

print ''.join([chr(i) for i in range(32, 127)])


import string as str_
import random

print str_.ascii_letters

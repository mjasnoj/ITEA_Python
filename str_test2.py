import string
import random

print dir(string)

print string.ascii_letters

print ''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)])

name = 'Bill'
age = 34

print "name: " + name + "; age: " + str(age)

print "Name: %s; age: %d" % (name, age)

print "name: {}; age: {}".format(name, age)
print "name: {0}; age: {1}".format(name, age)
print "name: {}; age: {:>20}".format(name, age)

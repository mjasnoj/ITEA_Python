class Cat(object):
    def say(self):
        print "Myaw"

class Dog(object):
    def say(self):
        print "Wow"

class Snake(object):
    def say(self):
        print "HHHH"

Zoo = [Cat(), Cat(), Dog(), Snake(), Cat()]
for animal in Zoo:
    animal.say()

print "-"*50

class Truck(object):
    def say(self):
        print "RRRR"

Zoo.append(Truck())

for animal in Zoo:
    animal.say()

print "-"*50

c = Cat()
print c                 ##  '__repr__' method

class Cat2(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):                                             # debug representation
        return "Cat('{}')".format(self.name)
    def __str__(self):                                              # object to string
        return "Cat {}".format(self.name)
    def say(self):
        print "Myaw"

c = Cat2('Thomas')
print c                 ## Python lloks for __str__, then __refer__, then looks for objects __refer__
print `c`               ## print __refer__

import pprint
pprint.pprint([1,2,3,[1,2,3,[1,2,3,[1,2,3,[1,2,3,[1,2,3,[1,2,3,[1,2,3,[1,2,3,[1,2,3]]]]]]]]]])

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

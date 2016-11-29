class A(object):
    def m1(self):
        print "A.m1"
    def m2(self):
        print "A.m2"
    def m3(self):
        print "A.m3"

class Proxy(object):
    def __init__(self):
        self._a = A()
    def m1(self):
        print "Proxy.m1"
    def __getattr__(self, name):
        return getattr(self._a, name)

XXX = Proxy()

XXX.m1()
XXX.m2()
XXX.m3()
# XXX.m4() - returns error

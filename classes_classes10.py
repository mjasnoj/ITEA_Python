class A(object):
    def __init__(self):
        #self.a = 42
        pass
    def __setattr__(self, name, value):
        #print "Set {} = {}".format(name, value)
        #if name == 'a':
        if hasattr(self, 'a') and name == 'a':
            raise AttributeError('a is read-only')
        super(A, self).__setattr__(name, value)
    def __delattr__(self, name):
        if name == 'a':
            raise AttributeError('a is read-only')
        super(A, self).__delattr__(name)
    def __getattribute__(self, name):
        print "Get attribute " + name
        return super(A, self).__getattribute__(name)
    def __getattr__(self, name):
        print "get attr " + name
        return 44


a = A()

print a.a
print a.b  # returns error

print "-"*50

#a.a = 43    # returns error

print "-"*50

#del a.a    # returns error

print "-"*50




class Mock(object):
    def __getattr__(self, name):
        return lambda x: x*x

m = Mock()
print m.f(2)

print m.wefwe(2)

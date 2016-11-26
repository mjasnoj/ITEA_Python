# class ClassName(object):
#    """docstring for ."""
#    def __init__(self, arg):
#        super(, self).__init__()
#        self.arg = arg

class Table(object):
    def __init__(self, l, w, h):
        print "Init"
        self.l = l
        self.w = w
        self.h = h

t = Table(100, 50, 60)

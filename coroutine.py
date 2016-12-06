# coding: utf-8

def coroutine(f):
    g = f()
    g.next()
    return g


@coroutine
def f():
    i = yield
    print 'f:', i
    i = yield i + 1
    print 'f:',i
    i = yield i + 1
    print 'f:',i
    i = yield i + 1


def main():
    i = f.send(0)
    print 'Main:', i
    i = f.send(i + 1)
    print 'Main:', i
    i = f.send(i + 1)
    print 'Main:', i

"""
>>> main()
f: 0
Main: 1
f: 2
Main: 3
f: 4
Main: 5

"""

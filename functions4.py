# coding=utf-8


def f_a():
    print 'Funt a'


def f_b():
    print 'Funt b'


def f_c():
    print 'Funt c'

action = raw_input("?")

d = {'a': f_a, 'b': f_b, 'c': f_c}
#d[action]()

def default():
    print 'default'

d.get(action, default)()                # default function as default value for get

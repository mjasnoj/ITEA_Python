# coding=utf-8

print "Module 1"

a = 2

if __name__ == '__main__':          # will be executed only if module launched as independent programm but not as imported module. For example for tests
    print __name__


def f():
    print a

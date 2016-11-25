# coding=utf-8


def get_area(x):
    return x * x


def scale(f):
    def wrapper(x):
        print "In"
        res = f(x / 100.0)
        print "Out"
        return res
    print "Scale"
    return wrapper


get_area = scale(get_area)
print get_area

print "----------------------"

print get_area(300)

print "----------------------"

@scale
def get_area2(x):
    return x * x

print get_area2(400)


print "#"*50

def scale(k):
    def decorator(f):
        def wrapper(x):
            return f(k * x)
        return wrapper
    return decorator

@scale(5)
def get_area3(x):
    return x * x

print get_area3(1)          # get_area3 = scale(5)(get_area3)       scale(5) -> decorator

print "#"*50

def logger(f):
    def wrapper(*args, **kwargs):
        print "Params: {}, {}".format(args, kwargs)
        res = f(*args, **kwargs)
        print "Result: {}".format(res)
        return res
    return wrapper

@logger
def f(a,b,c):
    return a + b + c

print f(1, 3, c = 15)

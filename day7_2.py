# coding: utf-8

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

"""
>>> import profile
>>> fib(20)
10946
>>> profile.run('fib(20)')
         21894 function calls (4 primitive calls) in 0.020 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
  21891/1    0.020    0.000    0.020    0.020 <stdin>:1(fib)
        1    0.000    0.000    0.020    0.020 <string>:1(<module>)
        1    0.000    0.000    0.020    0.020 profile:0(fib(20))
        0    0.000             0.000          profile:0(profiler)

"""

class memo(object):
    def __init__(self):
        self._state = {}
    def __call__(self, f):
        def wrapper(n):
            if n not in self._state:
                self._state[n] = f(n)
            return self._state[n]
        return wrapper

@memo()
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

"""
>>> import profile
>>> profile.run('fib(20)')
         63 function calls (5 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
     21/1    0.000    0.000    0.000    0.000 <stdin>:1(fib)
     39/1    0.000    0.000    0.000    0.000 <stdin>:5(wrapper)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 profile:0(fib(20))
        0    0.000             0.000          profile:0(profiler)


>>> fib(20)
10946

>>> profile.run('fib(20)')
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
        1    0.000    0.000    0.000    0.000 <stdin>:5(wrapper)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 profile:0(fib(20))
        0    0.000             0.000          profile:0(profiler)

"""

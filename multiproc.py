# coding: utf-8

import multiprocessing

a = 0

q = multiprocessing.Queue()

def f():
    global a
    for i in range(10000):
        a += 1
    q.put(a)


for i in range(100):
    p = multiprocessing.Process(target=f)
    p.start()

for i in range(100):
    a += q.get()

print a             # выведет 0 потому что все процессы работают в разном адресном пространстве


"""
IPC - Inter Process Communication

1. pipe
2. message queue            core object
3. shared mem               the fastest mechanism
4. sockets                  allow to communicate between servers

"""

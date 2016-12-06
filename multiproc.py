# coding: utf-8

import multiprocessing

a = 0

def f():
    global a
    for i in range(10000):
        a += 1

ps = []
for i in range(100):
    p = multiprocessing.Process(target=f)
    p.start()
    ps.append(p)

for p in ps:
    p.join

print a             # выведет 0 потому что все процессы работают в разном адресном пространстве

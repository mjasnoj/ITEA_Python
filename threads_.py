# coding: utf-8

# GIL - global interpretator Lock
# 100 внутренних комманд
# запрос к внешним ресурсам

# есть выхлоп если есть ожидания внешних ресурсов. во время ожидания выполняется другой поток.

import threading

a = 0

l = threading.Lock()

def hello():
    global a
    for i in range(10000):
        l.acquire()
        a += 1                      # необходимо гарантировать атамарность данного учатка кода
        l.release()

        #with l:
        #    a+=1

ts = []
for i in range(100):
    t = threading.Thread(target=hello)
    t.start()
    ts.append(t)


print a


for t in ts:
    t.join()

print a

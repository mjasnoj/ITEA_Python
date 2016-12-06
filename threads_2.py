import threading
import urllib2
import datetime

"""
for i in range(20):
    r = urllib2.urlopen('http://lifecell.ua/uk/')
    print len(r.read())
"""

t1 = datetime.datetime.now()

def get():
    r = urllib2.urlopen('http://lifecell.ua/uk/')
    print len(r.read())

ts = []
for i in range(20):
    t = threading.Thread(target=get)
    t.start()
    ts.append(t)

for t in ts:
    t.join()

t2 = datetime.datetime.now()

print "Time: ", t2 - t1

import threading
import urllib2
import datetime
import Queue

q = Queue.Queue()

def get():
    while True:
        url = q.get()
        r = urllib2.urlopen(url)
        print len(r.read())
        q.task_done()

t1 = datetime.datetime.now()

ts = []
for i in range(5):
    t = threading.Thread(target=get)
    t.start()

for j in range(20):
    q.put('http://lifecell.ua/uk/')

q.join()

t2 = datetime.datetime.now()

print "Time: ", t2 - t1

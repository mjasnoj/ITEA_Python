import threading
import urllib2
import datetime
import Queue

q = Queue.Queue()

is_finished = False

def get(i):
    while not is_finished:
        try:
            url = q.get(False)
            r = urllib2.urlopen(url)
            print i, len(r.read())
            q.task_done()
        except Queue.Empty:
            pass

t1 = datetime.datetime.now()

ts = []
for i in range(5):
    t = threading.Thread(target=get, args=(i,))
    t.start()

for j in range(20):
    q.put('http://lifecell.ua/uk/')

q.join()
is_finished = True


t2 = datetime.datetime.now()

print "Time: ", t2 - t1

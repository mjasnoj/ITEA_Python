import socket
import time
import sys

s = socket.socket()
s.connect(('10.132.14.62', 8000))
#s.connect(('127.0.0.1', 8000))

i = 1

while True:
    s.sendall('Hello Vlad %s' % i + sys.argv[1])
    data = s.recv(1024)

    print data

    i += 1

    time.sleep(1)

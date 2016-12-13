# coding: utf-8

import multiprocessing
import urllib2

def get(url):
    r = urllib2.urlopen(url)
    return len(r.read())

p = multiprocessing.Pool(20)                        # optimal poool size depends on Inet speed and response Time
print p.map(get, ['http://lifecell.ua/uk/']*20)




# multiproc - for calculations
# threads - for remote resources

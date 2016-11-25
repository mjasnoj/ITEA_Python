#coding=utf-8
with open('file.txt', 'rt') as f:
    for line in f:
        print line

print f.closed

""" оператор with создает контекст в рамках которого будет открыт файл"""

obj = [1, 'sad', [1, 2, 3], {'a': 3}]
print str(obj)

print "-"*20

import pickle               # for serialization

s = pickle.dumps(obj)
pickle.dump(obj, open('obj.pickle', 'wt'))
print s
print "-"*20

obj1 = pickle.loads(s)
print obj1
print "-"*20

obj2 = pickle.load(open('obj.pickle', 'rt'))
print obj2
print "-"*20

import json

s = json.dumps(obj)
print s

print json.loads(s)         # json serialization returns not the same object. String become Unicode

print "-"*20

import yaml

ss = yaml.dump(obj)
print ss

print yaml.load(ss)

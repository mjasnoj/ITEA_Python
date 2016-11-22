# coding=utf-8

d = {}
d = { 'a': 1, 'b': 'asdcsd'}

"""
Ключи не могут быть изменяемых типов: список и т.д.
"""

print d
d[0] = 'asdasds'
print d

""" Словарь упорядочен по хешу ключей"""

print hash(23)
print hash(99999999999999999999999999)
print hash('asdfsdcvasdfcd')

d['qwe'] = 3.12

print d

d['qwe'] = 45

print d

del d['qwe']

print d

print 'qwe' in d
print 0 in d

for k in d:
    print k

for k in d:
    print k, d[k]

for key, value in d.items():
    print key, value

print d.items()
print d.iteritems()

#print d[3]

if 3 in  d:
    print d[3]
else:
    print 0

print d.get('b', 3)
print d.get('c', 3)

print d.pop('b', 3)
print d.pop('b', 3)

if 'word' in d:
    d['word'] += 1
else:
    d['word'] = 1

print d

d.setdefault('word1', 42)
d.setdefault('word', 42)

print d

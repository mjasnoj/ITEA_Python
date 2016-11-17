l = [1,2,3,4]
l.append(5)

print l

print l.count(3)

l.extend([5,6,7])

print l

print l.index(3)

l.insert(0,32)

print l

print l.pop(5)

l.remove(2)

while 2 in l:
    l.remove(2)

l.reverse()
l.sort()

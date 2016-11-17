l = []
print l
l = [1,2,3,4]
print l

print len(l)
print l[0]
#print l[4]
print l[-1]
"""last element"""

l = [1,2,3,4,5,6,7,8]

print l[0:4]
print l[-3:]
print l[:4]
print l[:]
"""list copy"""

print l[::2]
print l[::-1]

l[2:5] = [7,8,9,0]

print l

l[0] = [1,2,3,4]

print l

l = [1,2,3]
l1 = l

print l1

l[0] = 0

print l[0]

l1 = [[1,2], 3, 4]

import copy
l = copy.copy(l1)

l[0][0] = 0
print l1

import string
import random

print dir(string)

print string.ascii_letters

print ''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)])

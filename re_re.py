import re

s = 'asfas das dfasd fs 0672393553 sdf s 067 239 35 53'

print re.findall(r"(\+?(38)?0?\d{2}\s?\d{3}[-,\s]?\d{2}[-,\s]?\d{2})", s)

r = re.match(r'(?P<msisdn>\+?(38)?0?\d{2}\s?\d{3}[-,\s]?\d{2}[-,\s]?\d{2})', '0632105679')

print r.groups()

r = re.search(r'(?P<msisdn>\+?(38)?0?\d{2}\s?\d{3}[-,\s]?\d{2}[-,\s]?\d{2})', s)

print r.groupdict()

print "-"*20

r = re.compile(r'(?P<msisdn>\+?(38)?0?\d{2}\s?\d{3}[-,\s]?\d{2}[-,\s]?\d{2})')                # for usage speedup and repeat

m = r.search(s)

print m.groupdict()

print "-"*20

print m.group(1)

#print r.groupdict(r"(\+?(38)?0?\d{2}\s?\d{3}[-,\s]?\d{2}[-,\s]?\d{2})", s)

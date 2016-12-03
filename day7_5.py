class Table(object):
    def __init__(self, id_):
        self.id = id_
    def __repr__(self):
        return 'Table:' + str(self.id)

class Chair(object):
    def __init__(self, id_):
        self.id = id_
    def __repr__(self):
        return 'Chair:' + str(self.id)

class Furniture(object):
    def __new__(cls, attrs):
        if attrs['type'] == u'Table':
            return Table(attrs['id'])
        elif attrs['type'] == u'Chair':
            return Chair(attrs['id'])
        else:
            raise ValueError

room = []
import json

d = [{'type': 'Table', 'id': 123}, {'type': 'Chair', 'id': 1234}]

s = json.dumps(d)

for f in json.loads(s):
    room.append(Furniture(f))

print room

"""
[Table:123, Chair:1234]
фабрика
"""

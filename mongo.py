>>> import pymongo
>>> m = pymongo.MongoClient()
>>> m.local.testcol.insert({'a':1, 'b':5, 'c':[1,2,3,4,5]})
ObjectId('58597ce49a40ca124084dfaf')

>>> m.local.testcol.find()
<pymongo.cursor.Cursor object at 0x7fdc8df1ec10>
>>> c = m.local.testcol.find()
>>> for doc in c:
...     print doc
...
{u'a': 1, u'c': [1, 2, 3, 4, 5], u'_id': ObjectId('58597ce49a40ca124084dfaf'), u'b': 5}

pip install elasticsearch

>>> import elasticsearch
>>> e = elasticsearch.Elasticsearch('10.1.15.47')
>>> doc = {'name': 'Product1', 'price': 1233}
>>> e.index(index='dpodugor', doc_type='product', id=1, body=doc)
{u'_type': u'product', u'_shards': {u'successful': 1, u'failed': 0, u'total': 2}, u'_index': u'dpodugor', u'_version': 1, u'created': True, u'result': u'created', u'_id': u'1'}


e.search(index='dpodugor', doc_type='product', body={'query':{'match_all':{}}})
{u'hits': {u'hits': [{u'_score': 1.0, u'_type': u'product', u'_id': u'1', u'_source': {u'price': 1233, u'name': u'Product1'}, u'_index': u'dpodugor'}], u'total': 1, u'max_score': 1.0}, u'_shards': {u'successful': 5, u'failed': 0, u'total': 5}, u'took': 2, u'timed_out': False}

>>> import redis
>>> r = redis.StrictRedis()
>>> r.set('a1', 1)
True
>>> r.get('a')
>>> r.get('a1')
'1'
>>> r.lrange('l', 0, -1)
[]
>>> r.lpush('l', 1)
1L
>>> r.lrange('l', 0, -1)
['1']

>>> import sqlite3
>>> con = sqlite3.connect('db.sqlite')
>>> con.execute("create table t(a int, b varchar(20))")
<sqlite3.Cursor object at 0x7fca2db4fa40>
>>> con.execute("insert into t (a, b) values (?, ?)", (1000, 'aaa'))
<sqlite3.Cursor object at 0x7fca2db4fab0>
>>> con.execute("insert into t (a, b) values (?, ?)", (1001, 'bbb'))
<sqlite3.Cursor object at 0x7fca2db4fa40>
>>> con.commit()


sqlite> select * from t;
sqlite> select * from t;
1000|aaa
1001|bbb


fetch - iterator

>>> c = con.execute('select * from t')
>>> c.fetchone()
(1000, u'aaa')
>>> c.fetchall()
[(1001, u'bbb')]
>>> c.fetchall()
[]

>>> c = con.execute('select * from t')
>>> for row in c:
...     print row
...
(1000, u'aaa')
(1001, u'bbb')

>>> fields = ('a', 'b')
>>> dict(zip(fields, row))
{'a': 1001, 'b': u'bbb'}









>>> import MySQLdb
>>> con = MySQLdb.connect(user='root', passwd='root',db='db1')
>>> cursor=con.cursor()
>>> cursor.execute("insert into t (a,b) values(1000,'aaa')")
1L
>>> cursor.execute("insert into t (a,b) values(2000,'bbb')")
1L
>>> con.commit()

>>> cursor.execute("select * from t")
2L
>>> for row in cursor:
...     print row
...
(1000L, 'aaa')
(2000L, 'bbb')





>>> from sqlalchemy.ext.automap import automap_base
>>> from sqlalchemy.orm import Session
>>> from sqlalchemy import create_engine
>>>
>>> Base = automap_base()
>>>
>>> engine = create_engine("mysql://root:root@127.0.0.1/db1")
>>> Base.prepare(engine, reflect=True)
>>> Base.classes.user
<class 'sqlalchemy.ext.automap.user'>

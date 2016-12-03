# coding: utf-8

"""
>>> import datetime
>>> d1 = datetime.datetime.now()
>>> d2 = datetime.datetime.now()
>>> d1
datetime.datetime(2016, 12, 3, 8, 21, 44, 601026)
>>> d2
datetime.datetime(2016, 12, 3, 8, 21, 47, 889113)
>>> d2 - d1
datetime.timedelta(0, 3, 288087)
>>> d1 + datetime.timedelta(days=10)
datetime.datetime(2016, 12, 13, 8, 21, 44, 601026)
>>> d1 + datetime.timedelta(days=30)
datetime.datetime(2017, 1, 2, 8, 21, 44, 601026)
"""

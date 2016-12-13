#coding=utf-8

class Table(object):
    def __init__(self, l, w, h):
        self.l, self.w, self.h = l, w, h

class ReprMixin(object):
    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join(["{}={}".format(k, v) for k, v in self.__dict__.items()])
        )


class TableWithBox(ReprMixin, Table):
    def __init__(self, *args, **kwargs):                      # если не задать инит он будет вызван из базового класса
        super(TableWithBox, self).__init__(*args, **kwargs)   # super - метод, возвращающий базовый класс. Дает возможность использовать конструктор базового класса.
        self.box_is_opened = False

t = Table(100, 50, 60)
print t
print vars(t)

print "-"*50

tt = TableWithBox(10, 50, 60)
print vars(tt)
print tt.__dict__

print tt

"""
TableWithBox(h=60, l=10, w=50, box_is_opened=False)
"""

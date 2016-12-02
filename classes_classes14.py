class ReprMixin(object):
  def __repr__(self):
    return '{}({})'.format(
      self.__class__.__name__,
      ', '.join(['{}={}'.format(k, v) for k, v in self.__dict__.items()])
    )

class Number(ReprMixin):
    def __init__(self, value):
        self.value = value
        

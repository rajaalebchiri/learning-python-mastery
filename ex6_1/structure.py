"""structure.py ex 6 1"""


class Structure:
    """ Structure Class """
    _fields = ()

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, arg in zip(self._fields, args):
            setattr(self, name, arg)

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, ", ".join(repr(getattr(self, name)) for name in self._fields))

    def __setattr__(self, name, value):
        if name.startswith("_") or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError("No attribute %s" % name)

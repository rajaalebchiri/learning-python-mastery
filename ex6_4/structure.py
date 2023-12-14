""" structure.py ex 6 4 """
import sys
import inspect


class Structure:
    """Structure class"""
    _fields = ()

    @classmethod
    def create_init(cls):
        locs = {}
        argstr = ','.join(cls._fields)
        code = f'def __init__(self, {argstr}):\n'
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'
        exec(code, locs)
        cls.__init__ = locs['__init__']

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, ", ".join(repr(getattr(self, name)) for name in self._fields))

    def __setattr__(self, name, value):
        if name.startswith("_") or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError("No attribute %s" % name)

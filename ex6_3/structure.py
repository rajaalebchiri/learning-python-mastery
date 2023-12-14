"""structure.py ex6_3"""
import sys
import inspect

class Structure:
    """Structure class"""
    _fields = ()

    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop("self")
        for name, val in locs.items():
            setattr(self, name, val)
    
    @classmethod
    def set_fields(cls):
        sig = inspect.signature(cls)
        cls._fields = tuple(sig.parameters)
        

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, ", ".join(repr(getattr(self, name)) for name in self._fields))

    def __setattr__(self, name, value):
        if name.startswith("_") or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError("No attribute %s" % name)

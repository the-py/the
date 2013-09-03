import sys
sys.path.append('../the')
from the import *

class Fake(object):
    def after(self, *args): pass
    def begin(self, *args): pass
    def ok(self, *args): pass
    def fail(self, *args): pass

world = World(None, Fake)
the = The

def safe(fn):
    def _fn(*args, **kwargs):
        world.errors = []
        return fn(*args, **kwargs)
    return _fn

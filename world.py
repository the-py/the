from context import Context
from copy import copy
from reporter import default, raw

class World(object):
    __instance = None

    def __new__(cls, error=None, reporter = default):
        if not cls.__instance:
            i = cls.__instance = super(World, cls).__new__(cls)
            i.message = error
            i.reporter = reporter
            i.errors = []
        if error:
            i.add(error)
        return cls.__instance

    def __enter__(self):
        Context().reset().stepin(self)
        return self
    begin = enter = __enter__

    def __exit__(self, etype=None, evalue=None, trace=None):
        self.reporter(self.errors)
        self.errors = []
        Context().reset()
        return True
    done = leave = __exit__

    def add(self, error, current=None):
        chain = copy(Context().chain)
        if current and not Context().current() == current:
            chain.append(current)
        self.errors.append([chain, error])
    append = add

TheTest = World

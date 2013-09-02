from copy import deepcopy

class Context(object):
    __instance = None
    def __new__(cls):
        if not cls.__instance:
            i = cls.__instance = super(Context, cls).__new__(cls)
            i.chain = []
        return cls.__instance

    def last(self):
        return self.chain[-2]

    def current(self):
        return self.chain[-1]

    def stepin(self, obj):
        self.chain.append(obj)

    def stepout(self):
        self.chain.pop()

    def reset(self):
        self.chain = []
        return self

class ContextException(Exception): pass

def skip():
    raise ContextException("get out of the context")


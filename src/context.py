from copy import deepcopy

class Context(object):
    instance = None
    def __new__(cls):
        if not cls.instance:
            i = cls.instance = super(Context, cls).__new__(cls)
            i.chain = []
        return cls.instance

    def __getattr__(self, attr):
        if attr == "current":
            return self.chain[-1]
        elif attr == "parent":
            return self.chain[-2]
        elif attr in ["set", "get", "after_each", "before_each", "only", "skip"]:
            return getattr(self.chain[-1], attr)
        else:
            raise AttributeError('No attribute ' + attr + ' found in Context.')

    def stepin(self, obj):
        self.chain.append(obj)

    def stepout(self):
        self.chain.pop()

    def reset_chain(self):
        self.chain = []
        return self

class ContextException(Exception): pass

def skip():
    raise ContextException("get out of the context")

def this():
    return Context().current

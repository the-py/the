import re

class The(object):
    them = {'should', 'to', 'have', 'has', 'must', 'be', 'And', 'when', 'but', 'it'}
    coders = {
        'nt': lambda obj: obj.__not(),
        'Not': lambda obj: obj.__not()
    }

    def __init__(self, obj):
        self.neg = False
        self.obj = obj
        self.__obj = None

    def __getattr__(self, attr):
        if attr in The.them:
            return self
        elif attr in The.coders:
            The.coders[attr](self)
            return self
        else:
            raise AttributeError('No attribute ' + attr + ' found.')

    def __enter__(self):
        return self

    def __exit__(self, etype, evalue, trace):
        # todo
        pass

    def __not(self):
        self.neg = not self.neg
        return self

    def check(self, stmt, msg=''):
        if self.neg:
            assert not stmt, msg
        else:
            assert stmt, msg
            return self

    def equal(self, value):
        return self.check(self.obj == value)

    def a(self, tp):
        return self.check(isinstance(self.obj, tp))
    an = a

    def exist(self):
        return self.check(self.obj)
    ok = exists = exist

    def true(self):
        return self.check(self.obj is True)

    def false(self):
        return self.check(self.obj is False)

    def empty(self):
        return not self.exist()

    def Is(self, other):
        return self.check(self.obj is other)

    def within(self, x, y=None):
        x = range(x, y) if y else x
        return self.check(self.obj in x)

    def above(self, n):
        return self.check(self.obj > above)

    def below(self, n):
        return self.check(self.obj < n)

    def match(self, regex):
        return self.check(re.search(regex, self.obj))

    def length(self, n):
        return self.check(len(self.obj) == n)
    size = length

    def item(self, key, value=None):
        self.check(key in self.obj)
        return self.check(self.obj[key] == value) if value else self

    def items(self, *args, **kwargs):
        for i in args:
            self.item(i)
        for key, value in kwargs.iteritems():
            self.item(key, value)
        return self

    def key(self, key):
        return self.item(key)

    def value(self, val):
        return self.check(val in self.obj.values())

    def keys(self, *args):
        # return self.check(reduce(lambda acc, x: acc and (x in self.obj),
        #                          args, True))
        for x in args:
            self.key(x)
        return self

    def values(self, *args):
        for x in args:
            self.value(x)
        return self

    def property(self, key, value=None):
        self.check(hasattr(self.obj, key))
        return self.check(getattr(self.obj, key) == value) if value else self
    attr = attribute = property

    def properties(self, *args, **kwargs):
        for i in args:
            self.property(i)
        for key, value in kwargs.iteritems():
            self.property(key, value)
        return self
    attrs = attributes = properties

    def include(self, item):
        return self.check(item in self.obj)

    def apply(self, *args, **kwargs):
        self.__obj = lambda : self.obj(*args, **kwargs)
        return self

    def Return(self, res):
        self.check((self.__obj or self.obj)() == res)
        self.__obj = None
        return self

    def respond_to(self, fn):
        return (self.check(hasattr(self.obj, fn)) and
                self.check(callable(getattr(self.obj, fn))))

    def throw(self, regex=None, tp=Exception):
        try:
            (self.__obj or self.obj)()
        except tp as e:
            if regex:
                self.check(re.search(regex, e.message))
        else:
            assert False, 'No exception found!'
        self.__obj = None
        return self

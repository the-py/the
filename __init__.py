import re

class The(object):
    them = {'should', 'to', 'have', 'must', 'be', 'and'}
    rockers = {'nt': lambda obj: obj.__not()}

    def __init__(self, obj):
        self.neg = False
        self.obj = obj
        self.__obj = None

    def check(self, stmt, msg=''):
        if self.neg:
            assert not stmt, msg
        else:
            assert stmt, msg
        return self

    def __getattr__(self, attr):
        if attr in The.them:
            return self
        elif attr in The.rockers:
            The.rockers[attr](self)
            return self
        else:
            raise AttributeError('No attribute ' + attr + ' found.')

    def equal(self, value):
        return self.check(self.obj == value)

    def a(self, type):
        return self.check(isinstance(self.obj, type))
    an = a

    def exist(self):
        return self.check(self.obj)
    exists = exist

    def __not(self):
        self.neg = not self.neg
        return self

    def ok(self):
        return self.exist()

    def true(self):
        return self.check(self.obj is True)

    def false(self):
        return self.check(self.obj is False)

    def empty(self):
        return self.exist()

    def _is(self, other):
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

    def property(self, key, value=None):
        self.check(self.obj.has_key(key))
        return value and self.check(self.obj[key] == value)
    key = property

    def include(self, item):
        return self.check(item in self.obj)

    def apply(self, *args, **kwargs):
        self.__obj = lambda : self.obj(*args, **kwargs)
        return self

    def keys(self, *args):
        # return self.check(reduce(lambda acc, x: acc and (x in self.obj),
        #                          args, True))
        for x in args:
            key(x)

    def throw(self, regex=None, type=Exception):
        try:
            (self.__obj or self.obj)()
        except type as e:
            if regex:
                self.check(re.search(regex, e.message))
        else:
            assert False, 'No exception found!'

        self.__obj = None
        return self

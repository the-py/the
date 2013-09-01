import re
import traceback
from world import World
from context import Context

class The(object):
    them = {'should', 'to', 'have', 'has', 'must', 'be', 'And', 'when', 'but', 'it'}
    coders = {
        'nt': lambda this: this.__not(),
        'true': lambda this: this.__check(this.obj is True,
                                      "{} is not True".format(this.obj)),
        'false': lambda this: this.__check(this.obj is False,
                                       "{} is not False".format(this.obj)),
        'none': lambda this: this.__check(this.obj is None,
                                      "{} is not None".format(this.obj)),
        'exist': lambda this: this.__check(this.obj is not None,
                                       "{} is None".format(this.obj)),
        'ok': lambda this: this.__check(this.obj),
        'empty': lambda this: this.__check(not this.obj)
    }
    coders['Not'] = coders['nt']
    coders['yes'] = coders['ok']
    coders['exists'] = coders['exist']

    def __init__(self, obj):
        self.neg = False
        self.message = self.obj = obj
        self.world = World()
        self.__obj = None         # for function call
        self.in_context = True

    def __call__(self, message):
        self.message = message
        return self

    def __getattr__(self, attr):
        if attr in The.them:
            return self
        elif attr in The.coders:
            The.coders[attr](self)
            return self
        else:
            raise AttributeError('No attribute ' + attr + ' found.')

    def __enter__(self):
        Context().stepin(self)
        return self

    def __exit__(self, etype=None, evalue=None, trace=None):
        Context().stepout()
        return True

    def __not(self):
        self.neg = True
        return self

    def __assert(self, stmt, msg):
        try:
            assert stmt, msg
        except Exception as e:
            self.world.append(traceback.format_stack() + [e.message])
        else:
            self.world.append(None)

    def __check(self, stmt, msg=''):
        if self.neg:
            self.__assert(not stmt, msg)
            self.neg = False
        else:
            self.__assert(stmt, msg)
        return self

    # ------------- api -----------------

    def equal(self, value):
        return self.__check(self.obj == value)

    def a(self, tp):
        return self.__check(isinstance(self.obj, tp),
                          "{} is not an instance of the {}".format(self.obj, tp.__name__))
    an = a

    def Is(self, other):
        return self.__check(self.obj is other, "{} is NOT {}".format(self.obj, other))

    def within(self, x, y=None):
        x = range(x, y) if y else x
        return self.__check(self.obj in x)

    def above(self, n):
        return self.__check(self.obj > above)

    def below(self, n):
        return self.__check(self.obj < n)

    def match(self, regex):
        return self.__check(re.search(regex, self.obj))

    def length(self, n):
        return self.__check(len(self.obj) == n)
    size = length

    def item(self, key, value=None):
        self.__check(key in self.obj)
        return self.__check(self.obj[key] == value) if value else self

    def items(self, *args, **kwargs):
        for i in args:
            self.item(i)
        for key, value in kwargs.iteritems():
            self.item(key, value)
        return self

    def key(self, key):
        return self.item(key)

    def value(self, val):
        return self.__check(val in self.obj.values())

    def keys(self, *args):
        for x in args:
            self.key(x)
        return self

    def values(self, *args):
        for x in args:
            self.value(x)
        return self

    def property(self, key, value=None):
        self.__check(hasattr(self.obj, key))
        return self.__check(getattr(self.obj, key) == value) if value else self
    attr = attribute = property

    def properties(self, *args, **kwargs):
        for i in args:
            self.property(i)
        for key, value in kwargs.iteritems():
            self.property(key, value)
        return self
    attrs = attributes = properties

    def include(self, item):
        return self.__check(item in self.obj)

    def apply(self, *args, **kwargs):
        self.__obj = lambda : self.obj(*args, **kwargs)
        return self

    def Return(self, res):
        fn = self.__obj or self.obj
        ret = fn()
        self.__check(ret == res, "{} is not equal to {}".format(str(ret), str(res)))
        return self

    def respond_to(self, fn):
        return (self.__check(hasattr(self.obj, fn)) and
                self.__check(callable(getattr(self.obj, fn))),
                str(self.obj), " not respond to " + fn)
    method = respond_to

    def throw(self, regex=None, tp=Exception):
        fn = self.__obj or self.obj
        try:
            fn()
        except tp as e:
            if regex:
                err = "{} throws <{} {}> not <{} {}>".format(self.obj,e.__class__.__name__, e.message, tp.__name__, regex)
                self.__check(re.search(regex, e.message), err)
        else:
            assert False, str(fn) + 'when called No exception throws!'
        return self

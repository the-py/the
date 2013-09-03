import re
import traceback
from context import Context, ContextException
from world import World



def what(var):
    s = '<' + var.__class__.__name__ + '>'
    if hasattr(var, "__name__"):
        s += var.__name__
    else:
        s += str(var)
    return s


class The(object):
    them = {'should', 'to', 'have', 'has', 'must', 'be', 'And', 'when', 'but', 'it'}
    coders = {
        'nt': lambda this: this.__not(),
        'true': lambda this: this.__check(this.obj is True,
                                          "{} is not True".format(what(this.obj))),
        'false': lambda this: this.__check(this.obj is False,
                                           "{} is not False".format(what(this.obj))),
        'none': lambda this: this.__check(this.obj is None,
                                          "{} is not None".format(what(this.obj))),
        'exist': lambda this: this.__check(this.obj is not None,
                                           "{} is None".format(what(this.obj))),
        # truthy
        'ok': lambda this: this.__check(this.obj,
                                        "{} is empty".format(what(this.obj))),
        # falsy
        'empty': lambda this: this.__check(not this.obj,
                                           "{} is not empty".format(what(this.obj)))
    }
    coders['Not'] = coders['nt']
    coders['yes'] = coders['ok']
    coders['exists'] = coders['exist']

    def __init__(self, obj):
        self.neg = False
        self.message = ''
        self.obj = obj
        self.__obj = None         # for function call

    def __call__(self, message=None):
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
        return False if etype and etype is not ContextException else True

    def __not(self):
        self.neg = True
        return self

    def __str__(self):
        return what(self.obj) + " " + self.message

    def __assert(self, stmt, msg):
        try:
            assert stmt, msg
        except AssertionError as e:
            World().reporter.fail(self, traceback.format_stack() + [e.message])
            World().append(traceback.format_stack() + [e.message])
        else:
            World().reporter.ok(self)
            World().append(None)

    def __check(self, stmt, msg=''):
        if self.neg:
            self.__assert(not stmt, msg)
            self.neg = False
        else:
            self.__assert(stmt, msg)
        return self

    # ------------- api -----------------

    def equal(self, value):
        return self.__check(self.obj == value,
                            what(self.obj) + " is not equal to " + what(value))

    def a(self, tp):
        return self.__check(isinstance(self.obj, tp),
                            "{} is not an instance of the {}".
                            format(what(self.obj), what(tp)))
    an = a

    def Is(self, other):
        return self.__check(self.obj is other,
                            "{} is NOT {}".format(what(self.obj), what(other)))

    def within(self, x, y=None):
        x = range(x, y) if y else x
        return self.__check(self.obj in x,
                            what(self.obj) + " is not in range of " + what(x))

    def above(self, n):
        return self.__check(self.obj > above,
                            what(self.obj) + " is not bigger than " + what(n))
    def below(self, n):
        return self.__check(self.obj < n,
                            what(self.obj) + " is not less than " + what(n))

    def match(self, regex):
        return self.__check(re.search(regex, self.obj))

    def length(self, n):
        return self.__check(len(self.obj) == n,
                            "the length of " + what(self.obj) + " is not " + n)
    size = length

    def item(self, key, value):
        return self.__check((key in self.obj) and (self.obj[key] == value),
                            "no such item {}: {}".format(key, what(value)))

    def items(self, **kwargs):
        ret = True
        for key, value in kwargs.iteritems():
            ret = ret and (key in self.obj) and (self.obj[key] == value)
        return self.__check(ret, what(self.obj) +
                            " doesn't contain " + what(kwargs))

    def key(self, key):
        return self.__check((key in self.obj),
                            what(self.obj) + " has no such key: " + key)

    def value(self, val):
        return self.__check(val in self.obj.values(),
                            what(self.obj) + " has no such value: " + what(val))

    def keys(self, *args):
        keys = self.keys()
        ret = all(map(lambda x: x in keys, args))
        return self.__check(ret, what(self.obj) +
                            " doesn't contain keys: " + what(args))

    def values(self, *args):
        values = self.values()
        ret = all(map(lambda x: x in values, args))
        return self.__check(ret, what(self.obj) +
                            " doesn't contain values: " + what(args))

    def property(self, key, value=None):
        ret = hasattr(self.obj, key)
        if value:
            ret = (getattr(self.obj, key) == value)
        return self.__check(ret,  "{} have no such property: {} => {}".
                            format(what(self.obj), what(key), what(value)))
    attr = attribute = property

    # def properties(self, *args, **kwargs):
    #     for i in args:
    #         self.property(i)
    #     for key, value in kwargs.iteritems():
    #         self.property(key, value)
    #     return self
    # attrs = attributes = properties

    def include(self, item):
        return self.__check(item in self.obj,
                            "{} does not include {}".
                            format(what(self.obj), what(item)))

    def apply(self, *args, **kwargs):
        self.__obj = lambda : self.obj(*args, **kwargs)
        return self

    def Return(self, res):
        fn = self.__obj or self.obj
        ret = fn()
        self.__check(ret == res, "{} is not equal to {}".format(what(ret), what(res)))
        return self

    def respond_to(self, fn):
        return self.__check(self.__check(hasattr(self.obj, fn)) and
                            self.__check(callable(getattr(self.obj, fn))),
                            what(self.obj) + " not respond to " + what(fn))
    method = respond_to

    def throw(self, regex=None, tp=Exception):
        fn = self.__obj or self.obj
        try:
            fn()
        except tp as e:
            if regex:
                err = "{} throws <{} {}> not <{} {}>".format(
                    self.obj,e.__class__.__name__, e.message, tp.__name__, regex)
                self.__check(re.search(regex, e.message), err)
        else:
            self.__check(False, what(fn) + 'when called No exception throws!')
        return self

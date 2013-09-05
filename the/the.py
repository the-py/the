import re

def inspect(var):
    s = '<' + var.__class__.__name__ + '>'
    if hasattr(var, "__name__"):
        s += var.__name__
    else:
        s += str(var)
    return s

def arginspect(args):
    ret = ",".join(map(lambda x: str(x), args[0]))
    for key, value in args[1].iteritems():
        ret += "," + str(key) + "=" + str(value)
    return "(" + ret + ")"


class The(object):
    them = {'should', 'to', 'have', 'has', 'must',
            'be', 'And', 'when', 'but', 'it'}

    coders = {'nt', 'true', 'false', 'none', 'exist',
              'ok', 'empty', 'Not', 'yes', 'exists',
              'truthy', 'falsy', 'no'}

    def __init__(self, obj):
        self.neg = False
        self.message = ''
        self.obj = obj
        self.args = [[], {}]

    def __call__(self, message=None):
        self.message = message
        return self

    def __getattr__(self, attr):
        if attr in The.them:
            return self
        elif attr in The.coders:
            self.__call_coder(attr)
            return self
        else:
            raise AttributeError('No attribute ' + attr + ' found.')

    def __enter__(self):
        return self

    def __exit__(self, etype=None, evalue=None, trace=None):
        pass

    def __call_coder(self, name):
        getattr(self, '_' + name)()

    def __str__(self):
        return inspect(self.obj) + " " + self.message

    def __assert(self, stmt, msg):
        assert stmt, msg

    def __check(self, stmt, msg=''):
        if self.neg:
            self.__assert(not stmt, msg)
            self.neg = False
        else:
            self.__assert(stmt, msg)
        return self

    # -- coder method --
    #
    # the following method are matchers(_nt not a matcher) but you don't call them explicitly
    # just write somthing like this:
    #    The(1).true
    #    The(1).Not.empty
    #
    # when you ref to this kind of attribute in the coders dict,
    # the object will try to prepend a '_' to the name of the attr
    # and call that method in return.
    # So that is to say, as the e.g. above,
    # When you say `true`, it will first check if it is in `self.coders`,
    # then find a method named as '_true' and call it.

    def _nt(self):
        self.neg = True
        return self
    _Not = _nt

    def _true(self):
        self.__check(self.obj is True,
                     "{} is not True".format(inspect(self.obj)))

    def _false(self):
        self.__check(self.obj is False,
                     "{} is not False".format(inspect(self.obj)))

    def _none(self):
        self.__check(self.obj is None,
                     "{} is not None".format(inspect(self.obj)))

    def _exist(self):
        self.__check(self.obj is not None,
                     "{} is None".format(inspect(self.obj)))
    _exists = _exist

    def _ok(self):
        self.__check(self.obj,
                     "{} is empty".format(inspect(self.obj)))
    _truthy = _yes = _ok

    def _empty(self):
        self.__check(not self.obj,
                     "{} is not empty".format(inspect(self.obj)))
    falsy = _no = _empty

    # ------------- api matchers -----------------

    def equal(self, value):
        return self.__check(self.obj == value,
                            inspect(self.obj) + " is not equal to " + inspect(value))
    equals = equal

    def a(self, tp):
        return self.__check(isinstance(self.obj, tp),
                            "{} is not an instance of the {}".
                            format(inspect(self.obj), inspect(tp)))
    an = a

    def Is(self, other):
        return self.__check(self.obj is other,
                            "{} is NOT {}".format(inspect(self.obj), inspect(other)))

    def is_not(self, other):
        return self.__check(self.obj is not other,
                            "{} IS {}".format(inspect(self.obj), inspect(other)))
    Is_not = is_not


    def above(self, n):
        return self.__check(self.obj > n,
                            inspect(self.obj) + " is not bigger than " + inspect(n))
    def below(self, n):
        return self.__check(self.obj < n,
                            inspect(self.obj) + " is not less than " + inspect(n))

    def match(self, regex):
        return self.__check(re.search(regex, self.obj))

    def length(self, n):
        return self.__check(len(self.obj) == n,
                            "the length of " + inspect(self.obj) +
                            " is not " + inspect(n))
    size = length

    def item(self, key, value):
        return self.__check((key in self.obj) and (self.obj[key] == value),
                            "no such item {}: {}".format(key, inspect(value)))

    def items(self, **kwargs):
        ret = True
        for key, value in kwargs.iteritems():
            ret = ret and (key in self.obj) and (self.obj[key] == value)
        return self.__check(ret, inspect(self.obj) +
                            " doesn't contain " + inspect(kwargs))

    def key(self, key):
        return self.__check((key in self.obj),
                            inspect(self.obj) + " has no such key: " + key)

    def value(self, val):
        return self.__check(val in self.obj.values(),
                            inspect(self.obj) + " has no such value: " + inspect(val))

    def keys(self, *args):
        keys = self.obj.keys()
        ret = all(map(lambda x: x in keys, args))
        return self.__check(ret, inspect(self.obj) +
                            " doesn't contain keys: " + inspect(args))

    def values(self, *args):
        values = self.obj.values()
        ret = all(map(lambda x: x in values, args))
        return self.__check(ret, inspect(self.obj) +
                            " doesn't contain values: " + inspect(args))

    def property(self, key, value=None):
        ret = hasattr(self.obj, key)
        if value:
            ret = (getattr(self.obj, key) == value)
        return self.__check(ret,  "{} have no such property: {} => {}".
                            format(inspect(self.obj), inspect(key), inspect(value)))
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
                            format(inspect(self.obj), inspect(item)))
    contains = contain = includes = include

    def within(self, items):
        return self.__check(self.obj in items,
                            "{} is not in {}".
                            format(inspect(self.obj), inspect(items)))
    In = within


    def apply(self, *args, **kwargs):
        self.args = [args, kwargs]
        return self

    def Return(self, res):
        try:
            ret = self.obj(*self.args[0], **self.args[1])
        except Exception as e:
            self.__check(False, "{} when called by {} throws an exception: {}".
                         format(inspect(self.obj), arginspect(self.args), e))
        else:
            self.__check(ret == res, "{} when called by {} is equal to {} not {}".
                         format(inspect(self.obj), arginspect(self.args),
                                inspect(ret), inspect(res)))
        return self

    def respond_to(self, fn):
        return self.__check(self.__check(hasattr(self.obj, fn)) and
                            self.__check(callable(getattr(self.obj, fn))),
                            inspect(self.obj) + " not respond to " + inspect(fn))
    method = respond_to

    def throw(self, regex=None, tp=Exception):
        try:
            self.obj(*self.args[0], **self.args[1])
        except tp as e:
            if regex:
                self.__check(re.search(regex, e.message),
                             "{} when called by {} throws <{} {}> not <{} {}>".
                             format(inspect(self.obj), arginspect(self.args),
                                    e.__class__.__name__, e.message,
                                    tp.__name__, regex))
        else:
            self.__check(False, '{} when called by {} No exception throws!'.
                         format(inspect(self.obj, arginspect(self.args))))
        return self

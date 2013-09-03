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

def args_detail(args):
    ret = ",".join(map(lambda x: str(x), args[0]))
    for key, value in args[1].iteritems():
        ret += "," + str(key) + "=" + str(value)
    return "(" + ret + ")"


class The(object):
    them = {'should', 'to', 'have', 'has', 'must', 'be', 'And', 'when', 'but', 'it'}
    coders = {'nt', 'true', 'false', 'none', 'exist', 'ok', 'empty', 'Not', 'yes', 'exists'}

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
        Context().stepin(self)
        return self

    def __exit__(self, etype=None, evalue=None, trace=None):
        Context().stepout()
        return False if etype and etype is not ContextException else True

    def __call_coder(self, name):
        getattr(self, '_' + name)()

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
                     "{} is not True".format(what(self.obj)))

    def _false(self):
        self.__check(self.obj is False,
                     "{} is not False".format(what(self.obj)))

    def _none(self):
        self.__check(self.obj is None,
                     "{} is not None".format(what(self.obj)))

    def _exist(self):
        self.__check(self.obj is not None,
                     "{} is None".format(what(self.obj)))
    _exists = _exist

    def _ok(self):
        self.__check(self.obj,
                     "{} is empty".format(what(self.obj)))
    _yes = _ok

    def _empty(self):
        self.__check(not self.obj,
                     "{} is not empty".format(what(self.obj)))

    # ------------- api matchers -----------------

    def equal(self, value):
        return self.__check(self.obj == value,
                            what(self.obj) + " is not equal to " + what(value))
    equals = equal

    def a(self, tp):
        return self.__check(isinstance(self.obj, tp),
                            "{} is not an instance of the {}".
                            format(what(self.obj), what(tp)))
    an = a

    def Is(self, other):
        return self.__check(self.obj is other,
                            "{} is NOT {}".format(what(self.obj), what(other)))

    def above(self, n):
        return self.__check(self.obj > n,
                            what(self.obj) + " is not bigger than " + what(n))
    def below(self, n):
        return self.__check(self.obj < n,
                            what(self.obj) + " is not less than " + what(n))

    def match(self, regex):
        return self.__check(re.search(regex, self.obj))

    def length(self, n):
        return self.__check(len(self.obj) == n,
                            "the length of " + what(self.obj) +
                            " is not " + what(n))
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
        keys = self.obj.keys()
        ret = all(map(lambda x: x in keys, args))
        return self.__check(ret, what(self.obj) +
                            " doesn't contain keys: " + what(args))

    def values(self, *args):
        values = self.obj.values()
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
    contains = contain = includes = include

    def within(self, items):
        return self.__check(self.obj in items,
                            "{} is not in {}".
                            format(what(self.obj), what(items)))
    In = within


    def apply(self, *args, **kwargs):
        self.args = [args, kwargs]
        return self

    def Return(self, res):
        try:
            ret = self.obj(*self.args[0], **self.args[1])
        except Exception as e:
            self.__check(False, "{} when called by {} throws an exception: {}".
                         format(what(self.obj), args_detail(self.args), e))
        else:
            self.__check(ret == res, "{} when called by {} is equal to {} not {}".
                         format(what(self.obj), args_detail(self.args),
                                what(ret), what(res)))
        return self

    def respond_to(self, fn):
        return self.__check(self.__check(hasattr(self.obj, fn)) and
                            self.__check(callable(getattr(self.obj, fn))),
                            what(self.obj) + " not respond to " + what(fn))
    method = respond_to

    def throw(self, regex=None, tp=Exception):
        try:
            self.obj(*self.args[0], **self.args[1])
        except tp as e:
            if regex:
                self.__check(re.search(regex, e.message),
                             "{} when called by {} throws <{} {}> not <{} {}>".
                             format(what(self.obj), args_detail(self.args),
                                    e.__class__.__name__, e.message,
                                    tp.__name__, regex))
        else:
            self.__check(False, '{} when called by {} No exception throws!'.
                         format(what(self.obj, args_detail(self.args))))
        return self

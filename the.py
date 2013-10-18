import re


class The(object):
    them = {'should', 'to', 'have', 'has', 'must',
            'And', 'when', 'but', 'it'}

    coders = {'nt', 'true', 'false', 'none', 'exist',
              'ok', 'empty', 'Not', 'NOT', 'not_to', 'should_not',
              'yes', 'exists', 'truthy', 'falsy', 'no'}

    def __init__(self, obj):
        self.neg = False
        self.obj = obj
        self.args = [[], {}]
        self.be = _TheBe(self)

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

    def __str__(self):
        return _inspect(self.obj)

    def __eq__(self, other):
        return self.eq(other)

    def __lt__(self, other):
        return self.lt(other)

    def __gt__(self, other):
        return self.gt(other)

    def __le__(self, other):
        return self.le(other)

    def __ge__(self, other):
        return self.ge(other)

    def __ne__(self, other):
        return self.ne(other)

    def __contains__(self, other):
        self.include(other)
        return self

    def __getitem__(self, key):
        return The(self.obj[key])

    def __assert(self, stmt, msg):
        assert stmt, msg

    def __check(self, stmt, msg=''):
        if self.neg:
            self.__assert(not stmt, msg)
            self.neg = False
        else:
            self.__assert(stmt, msg)
        return self

    def __call_coder(self, name):
        getattr(self, '_' + name)()

    # -- coder method --
    #
    # the following method are matchers(except `should_not`) but you don't
    # have to call them explicitly just write somthing like this will work:
    #    The(1).true
    #    The(1).Not.empty
    #
    # when you ref to this kind of attribute in the coders dict,
    # the object will try to prepend a '_' to the name of the attr
    # and call that method in return.
    #
    # So as in the e.g. above,
    # When you say `true`, it will first check if it is in `self.coders`,
    # then find a method named as '_true' and call it.

    def _should_not(self):
        self.neg = True
        return self
    _not_to = _NOT = _should_not

    def _true(self):
        self.__check(self.obj is True,
                     "{} is not True".format(_inspect(self.obj)))

    def _false(self):
        self.__check(self.obj is False,
                     "{} is not False".format(_inspect(self.obj)))

    def _none(self):
        self.__check(self.obj is None,
                     "{} is not None".format(_inspect(self.obj)))

    def _exist(self):
        self.__check(self.obj is not None,
                     "{} is None".format(_inspect(self.obj)))

    def _ok(self):
        self.__check(self.obj,
                     "{} is empty".format(_inspect(self.obj)))

    def _empty(self):
        self.__check(not self.obj,
                     "{} is not empty".format(_inspect(self.obj)))

    # ------------- api matchers -----------------

    def eq(self, value):
        return self.__check(self.obj == value,
                            _inspect(self.obj) +
                            " is not == " + _inspect(value))
    equal = eq

    def gt(self, n):
        return self.__check(self.obj > n,
                            _inspect(self.obj) +
                            " is not > " + _inspect(n))
    above = gt

    def lt(self, n):
        return self.__check(self.obj < n,
                            _inspect(self.obj) +
                            " is not < " + _inspect(n))
    below = lt

    def ge(self, n):
        return self.__check(self.obj >= n,
                            _inspect(self.obj) +
                            " is not >= " + _inspect(n))

    def le(self, n):
        return self.__check(self.obj <= n,
                            _inspect(self.obj) +
                            " is not <= " + _inspect(n))

    def ne(self, n):
        return self.__check(self.obj != n,
                            _inspect(self.obj) +
                            " is not != " + _inspect(n))

    def a(self, tp):
        return self.__check(isinstance(self.obj, tp),
                            "{} is not an instance of the {}".
                            format(_inspect(self.obj), _inspect(tp)))
    an = a

    def same_as(self, other):
        return self.__check(self.obj is other,
                            "{} is NOT {}".format(_inspect(self.obj),
                                                  _inspect(other)))

    def match(self, regex):
        return self.__check(re.search(regex, self.obj),
                            "{} and {} don't match".format(regex, self.obj))

    def length(self, n):
        return self.__check(len(self.obj) == n,
                            "the length of " + _inspect(self.obj) +
                            " is not " + _inspect(n))
    size = length

    def item(self, key, value):
        return self.__check((key in self.obj) and (self.obj[key] == value),
                            "no such item {}: {}".format(key, _inspect(value)))

    def items(self, **kwargs):
        for key, value in kwargs.items():
            self.item(key, value)
        return self

    def key(self, key):
        return self.__check((key in self.obj),
                            _inspect(self.obj) + " has no such key: " + key)

    def value(self, val):
        return self.__check(val in self.obj.values(),
                            _inspect(self.obj) +
                            " has no such value: " + _inspect(val))

    def keys(self, *args):
        for key in args:
            self.key(key)
        return self

    def values(self, *args):
        for value in args:
            self.value(value)
        return self

    def property(self, key, value=None):
        ret = hasattr(self.obj, key)
        if value:
            ret = (getattr(self.obj, key) == value)
        return self.__check(ret,  "{} have no such property: {} = {}".
                            format(_inspect(self.obj),
                                   _inspect(key), _inspect(value)))
    attr = attribute = property

    def properties(self, *args, **kwargs):
        for i in args:
            self.property(i)
        for key, value in kwargs.items():
            self.property(key, value)
        return self
    attrs = attributes = properties

    def include(self, item):
        return self.__check(item in self.obj,
                            "{} does not include {}".
                            format(_inspect(self.obj), _inspect(item)))
    contain = include

    def within(self, items):
        return self.__check(self.obj in items,
                            "{} is not in {}".
                            format(_inspect(self.obj), _inspect(items)))

    def inherit(self, c):
        return self.__check(issubclass(self.obj, c),
                            "{} is not subclass of {}".
                            format(_inspect(self.obj), _inspect(c)))

    def apply(self, *args, **kwargs):
        self.args = [args, kwargs]
        return self

    def result(self, res):
        try:
            ret = self.obj(*self.args[0], **self.args[1])
        except Exception as e:
            self.__check(False, "{} when called by {} throws an exception: {}".
                         format(_inspect(self.obj), _arginspect(self.args), e))
        else:
            self.__check(ret == res,
                         "{} when called by {} is equal to {} not {}".
                         format(_inspect(self.obj), _arginspect(self.args),
                                _inspect(ret), _inspect(res)))
        return self

    def method(self, fn):
        return self.__check(self.__check(hasattr(self.obj, fn)) and
                            self.__check(callable(getattr(self.obj, fn))),
                            _inspect(self.obj) +
                            " not respond to " + _inspect(fn))

    def throw(self, regex=None, tp=Exception):
        try:
            self.obj(*self.args[0], **self.args[1])
        except tp as e:
            if regex:
                self.__check(re.search(regex, str(e)),
                             "{} when called by {} throws <{} {}> not <{} {}>".
                             format(_inspect(self.obj), _arginspect(self.args),
                                    e.__class__.__name__, str(e),
                                    tp.__name__, regex))
        else:
            self.__check(False, '{} when called by {} No exception throws!'.
                         format(_inspect(self.obj, _arginspect(self.args))))
        return self

    @classmethod
    def exception(cls, regex=None, tp=Exception):
        return _TheBlock(regex, tp)

# should style, expect style
the = expect = The

class _TheBlock(object):
    def __init__(self, regex=None, tp=Exception):
        self.regex = regex
        self.tp = tp

    def __enter__(self):
        pass

    def __exit__(self, etype=None, evalue=None, trace=None):
        if not etype:
            assert False, "No exception throws!"
        expect(etype).inherit(self.tp)
        if self.regex:
            expect(str(evalue)).match(self.regex)
        return True

class _TheBe(object):
    def __init__(self, the):
        self.the = the

    def __call__(self, obj):
        return self.the.same_as(obj)

    def __getattr__(self, attr):
        return getattr(self.the, attr)

# --- helper methods ---

def _inspect(var):
    if var is None:
        return "None"
    if not hasattr(var, "__class__"):
        return str(var)
    s = '<' + var.__class__.__name__ + '>'
    if hasattr(var, "__name__"):
        s += var.__name__
    else:
        s += str(var)
    return s


def _arginspect(args):
    ret = ",".join(map(lambda x: str(x), args[0]))
    for key, value in args[1].items():
        ret += "," + str(key) + "=" + str(value)
    return "(" + ret + ")"

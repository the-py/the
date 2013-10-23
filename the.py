import re
import inspect


class _TheBe(object):
    def __init__(self, the):
        self.the = the

    def __call__(self, obj):
        return self.the._check(self.the.obj is obj,
                               _msg("{} is {}", self.the.obj, obj),
                               _msg("{} is not {}", self.the.obj, obj))

    def __getattr__(self, attr):
        return getattr(self.the, attr)


class _TheA(object):
    def __init__(self, the):
        self.the = the

    def __call__(self, tp):
        return self.the._check(isinstance(self.the.obj, tp),
                               _msg("{} is an instance of {}",
                                    self.the.obj, tp),
                               _msg("{} is not an instance of {}",
                                    self.the.obj, tp))

    def __getattr__(self, attr):
        return getattr(self.the, attr)


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


class The(object):
    this = {'should', 'to', 'have', 'when'}

    exe = {'true', 'false', 'none', 'exist',
              'ok', 'empty', 'NOT', 'not_to', 'should_not'}

    def __init__(self, obj):
        self.neg = False
        self.obj = obj
        self.args = [[], {}]
        self.be = _TheBe(self)
        self.an = self.a = _TheA(self)

    def __getattr__(self, attr):
        if attr in The.this:
            return self
        elif attr in The.exe:
            self.__call_coder(attr)
            return self
        else:
            raise AttributeError('No attribute ' + attr + ' found.')

    def __enter__(self):
        return self

    def __exit__(self, etype=None, evalue=None, trace=None):
        pass

    def __str__(self):
        return _i(self.obj)

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
        return True

    def __getitem__(self, key):
        self.key(key)
        if key in self.obj:
            return The(self.obj[key])
        return self

    def _check(self, stmt, msg='', negmsg=''):
        if self.neg:
            assert (not stmt), "EXPECT: " + negmsg
            self.neg = False
        else:
            assert stmt, "EXPECT: " + msg
        return self

    def __call_coder(self, name):
        getattr(self, '_' + name)()

    # -----
    # the following methods are matchers(except `should_not`) but you don't
    # have to call them explicitly. Instead write somthing like this will
    # trigger the corresponding matcher methods.
    #
    #    The(1).true
    #    The(1).NOT.empty
    #
    # When you ref to this kind of attribute in the exe dict,
    # it will try to prepend a '_' to the name of the attr
    # and call that method for you.
    #
    # As in the e.g. above,
    # When you say `true`, it will first check if it is in `self.exe`,
    # then find a method named as '_true' and call it.
    # ----

    def _should_not(self):
        self.neg = True
        return self
    _not_to = _NOT = _should_not

    def _true(self):
        return self._check(self.obj is True,
                           _msg("{} is True", self.obj),
                           _msg("{} is not True", self.obj))

    def _false(self):
        return self._check(self.obj is False,
                           _msg("{} is False", self.obj),
                           _msg("{} is not False", self.obj))

    def _none(self):
        return self._check(self.obj is None,
                           _msg("{} is None", self.obj),
                           _msg("{} is not None", self.obj))

    def _exist(self):
        return self._check(self.obj is not None,
                           _msg("{} is not None", self.obj),
                           _msg("{} is None", self.obj))

    def _ok(self):
        return self._check(self.obj,
                           _msg("{} is not empty", self.obj),
                           _msg("{} is empty", self.obj))

    def _empty(self):
        return self._check(not self.obj,
                           _msg("{} is empty", self.obj),
                           _msg("{} is not empty", self.obj))

    # ------------- api matchers -----------------

    def eq(self, n):
        return self._check(self.obj == n,
                           _msg("{} is equal to {}", self.obj, n),
                           _msg("{} is not equal to {}", self.obj, n))
    equal = eq

    def gt(self, n):
        return self._check(self.obj > n,
                           _msg("{} is greater than {}", self.obj, n),
                           _msg("{} is not greater than {}", self.obj, n))
    above = gt

    def lt(self, n):
        return self._check(self.obj < n,
                           _msg("{} is less than {}", self.obj, n),
                           _msg("{} is not less than {}", self.obj, n))
    below = lt

    def ge(self, n):
        return self._check(self.obj >= n,
                           _msg("{} is greater than or equal to {}",
                                self.obj, n),
                           _msg("{} is not greater than or equal to {}",
                                self.obj, n))

    def le(self, n):
        return self._check(self.obj <= n,
                           _msg("{} is less than or equal to {}", self.obj, n),
                           _msg("{} is not less than or equal to {}",
                                self.obj, n))

    def ne(self, n):
        return self._check(self.obj != n,
                           _msg("{} is not equal to {}", self.obj, n),
                           _msg("{} is equal to {}", self.obj, n))

    def match(self, regex):
        return self._check(re.search(regex, self.obj),
                           _msg("{} match {}", self.obj, regex),
                           _msg("{} do not matches {}", self.obj, regex))

    def length(self, n):
        return self._check(len(self.obj) == n,
                           _msg("the length of {} is {}", self.obj, n),
                           _msg("the length of {} is not {}", self.obj, n))
    size = length

    def item(self, **kwargs):
        return self.contain(kwargs)
    items = item

    def contain(self, subdict):
        for key, value in subdict.items():
            self._check((key in self.obj) and (self.obj[key] == value),
                        _msg("{} have item '{} = {}'", self.obj, key, value),
                        _msg("{} do not have item '{} = {}'",
                             self.obj, key, value))
        return self

    def key(self, *keys):
        for key in keys:
            self._check((key in self.obj),
                        _msg("{} have key '{}'", self.obj, key),
                        _msg("{} do not have key '{}'", self.obj, key))
        return self
    keys = key

    def value(self, *vals):
        for val in vals:
            self._check(val in self.obj.values(),
                        _msg("{} have value: {}", self.obj, val),
                        _msg("{} do not have value: {}", self.obj, val))
        return self
    values = value

    def property(self, *args, **kwargs):
        keys = kwargs.keys()
        for key in args:
            self._check(hasattr(self.obj, key),
                        _msg("{} have property: {}.", self.obj, key),
                        _msg("{} do not have property: {}.", self.obj, key))
        for key in keys:
            value = kwargs[key]
            self._check(getattr(self.obj, key) == value,
                        _msg("{} have property: {} = {}",
                             self.obj, key, value),
                        _msg("{} have property: {} = {}",
                             self.obj, key, value))
        return self
    properties = property

    def include(self, item):
        return self._check(item in self.obj,
                           _msg("{} include {}", self.obj, item),
                           _msg("{} do not include {}", self.obj, item))

    def within(self, items):
        return self._check(self.obj in items,
                           _msg("{} is an item of {}", self.obj, items),
                           _msg("{} is not an item of {}", self.obj, items))

    def inherit(self, c):
        return self._check(issubclass(self.obj, c),
                           _msg("{} is a subclass of {}", self.obj, c),
                           _msg("{} is not a subclass of {}", self.obj, c))

    def apply(self, *args, **kwargs):
        self.args = [args, kwargs]
        return self

    def result(self, res):
        msg = "{} when called by {} is equal to {}"
        msg = msg.format(_i(self.obj), _ai(self.args), _i(res))
        nemsg = "{} when called by {} is not equal to {}"
        nemsg = nemsg.format(_i(self.obj), _ai(self.args), _i(res))

        try:
            ret = self.obj(*self.args[0], **self.args[1])
        except Exception:
            self._check(False, msg, nemsg)
        else:
            self._check(ret == res, msg, nemsg)

        return self

    def method(self, fn):
        ret = hasattr(self.obj, fn) and callable(getattr(self.obj, fn))
        return self._check(ret,
                           _msg("{} have method: {}", self.obj, fn),
                           _msg("{} do not thave method: {}", self.obj, fn))

    def throw(self, regex=None, tp=Exception):
        msg = "{} when called by {} throw <{} {}>"
        msg = msg.format(_i(self.obj), _ai(self.args), tp.__name__, regex)
        nemsg = "{} when called by {} do not throw <{} {}>"
        nemsg = nemsg.format(_i(self.obj), _ai(self.args), tp.__name__, regex)

        try:
            self.obj(*self.args[0], **self.args[1])
        except tp as e:
            if regex:
                self._check(re.search(regex, str(e)), msg, nemsg)
        except Exception as e:
            self._check(False, msg, nemsg)
        else:
            self._check(False, msg, nemsg)

        return self

    @classmethod
    def exception(cls, regex=None, tp=Exception):
        return _TheBlock(regex, tp)

    @classmethod
    def use(cls, *args, **kwargs):
        for item in args:
            if inspect.ismodule(item):
                cls.use(item.API)
            elif isinstance(item, list):
                cls.use(*item)
            elif isinstance(item, dict):
                _add_method(item)
            elif isinstance(item, str):
                cls.this.add(item)
            else:
                _add_method({item.__name__: item})
        _add_method(kwargs)

# should style, expect style
the = expect = The


# --- helper methods ---

def _add_method(methods):
    for name, method in methods.items():
        if not _have_args(method):
            The.exe.add(name)
            name = "_" + name
        setattr(The, name, method)


def _have_args(fn):
    spec = inspect.getargspec(fn)
    args = spec.args[1:]
    return bool(args) or spec.varargs or spec.keywords


def _msg(msg, *args):
    args = [_i(arg) for arg in args]
    return msg.format(*args)


def _i(var):
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


def _ai(args):
    ret = ",".join(map(lambda x: str(x), args[0]))
    for key, value in args[1].items():
        ret += "," + str(key) + "=" + str(value)
    return "(" + ret + ")"

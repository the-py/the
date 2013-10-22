# A python assertion module for better assertion.

inspired by should.js and chai.js

# install
```shell
pip install the
```

# API
It provides one object called `the` with an alias `expect`.
(Take a look at the Usage and Example.)

```python
from the import the, expect
```

### Chains
> do nothing but return itself.

* `should`
* `have`
* `to`
* `when`

##### More chains?
```python
the.use("mychain")
```

### Matchers without arg
> trigger a certain assertion.

* `true`
* `false`
* `none`
* `exist`
* `ok`
* `empty`

##### More?
> take a look at the-easytype lib.

```python
# define your matcher
def happy(self):
    return self._check(self.obj == "happy",
                       self.obj + " is happy.",
                       self.obj + " is not happy.")

# add to `the`
the.use(happy)

# DONE!
the(string).should.be.happy
```

### Matchers with args
> trigger a certain assertion

* `eq(other)`, `equal(other)`
@param: other {mixed}  
assert equal(==)  
* `lt(other)`, `below(other)`
@param: other {mixed}  
assert less than(<)
* `gt(other)`, `above(other)`
> @param: other {mixed}
> assert greater than(<)
* `ne(other)`
> @param: other {mixed}
> assert not equal(!=)
* `le(other)`
> @param: other {mixed}
> assert less than
* `ge(other)`
> @param: other {mixed}
> assert greater than
* `match(regex)`
> @param: regex {mixed}
> assert string match a regex
* `length(n)`, `size(n)`
> @param: n {int}
> assert length
* `item`, `items`
> @param: **kwargs
> assert dict have item(s)
* `contain`
* `key`, `keys`
* `value`, `values`
* `property`, `properties`
* `include`
* `within`
* `inherit`
* `method`
* `result`(used to assert function return value using `apply` to apply args)
* `throw` (used to assert function throw exception using `apply` to apply args)
* `exception` ( assert exception throw. _classmethod_)

##### More?
> take a look at the-fs lib.

```python
# define your matcher
def firstname(self, name):
      fname = self.obj.split()[0]
      return self._check(fname == name,
                         "The firstname of {} is {}".format(self.obj, name),
                         "The firstname of {} is not {}".format(self.obj, name))

# add to `the`
the.use(firname)

# DONE!
expect("Wenjun Yan").to.have.firstname("Wenjun")
```

### Magic methods
* `==`
* `!=`
* `>=`
* `<=`
* `>`
* `<`
* `1 in the(range(1, 3))`

### Negations

* `NOT`
* `not_to`
* `should_not`


# Usage and Examples

### assert `>`, `<`, `>=`, `<=`, `==`

```python
expect(1) > 0
expect(1).gt(0)
expect(1).above(0)

expect(1) >= 0
expect(1).ge(0)

expect(1) < 2
expect(1).lt(0)
expect(1).below(0)

expect(1) <= 2
expect(1).le(0)

expect(1) == 1
expect(1).eq(1)
expect(1).equal(1)
```

### assert `True`, `False`, `None`
```python
the(True).should.be.true
expect(True).to.be.true

the(False).should.be.false
expect(False).to.be.false

the(None).should.be.none
expect(None).to.be.none
```

### assert `truthy`, `falsy`
```python
the(1).should.be.ok
expect(1).to.be.ok

the("").should.be.empty
expect("").to.be.empty
```

### assert `is`
```python
the(1).should.be(1)
expect(1).to.be(1)
```

### assert `isinstance`
```python
the(1).should.be.an(int)
expect("1").to.be.a(str)
```

### assert `issubclass`
```python
the(int).should.inherit(object)
expect(int).to.inherit(object)
```

### assert `in`
```python
the(1).should.be.within(range(1,3))
expect(1).to.be.within(range(1,3))
```

### assert `len`
```python
the(range(1, 3)).should.have.length(3)
expect(range(1, 3)).to.have.length(3)
```

### assert `regexp`
```python
the("abc").should.match("a")
expect("abc").to.match("a")
```

### assert `dict.item`
```python
d = {a: 1, b: 2}
the(d).should.have.items(a=1, b=2)
expect(d).to.have.items(a=1, b=2)

the(d).should.contain({"a": 1, "b": 2})
expect(d).to.contain({"a": 1, "b": 2})
```

### assert `dict.key`
```python
d = {a: 1, b: 2}
the(d).should.have.key("a")
expect(d).to.have.keys("a", "b")
```

### assert `dict.value`
```python
d = {a: 1, b: 2}
the(d).should.have.value(1)
expect(d).to.have.values(1, 2)
```

### assert `property`
```python
class A(object):
    def __init__(self):
        self.x = 1

    def getx(self):
        return self.x

expect(A()).to.have.property("x")
expect(A()).to.have.property(x=1)
```

### assert `method`
```python
class A(object):
    def __init__(self):
        self.x = 1

    def getx(self):
        return self.x

expect(A()).to.have.method("getx")
the(A()).should.have.method("getx")
```

### assert `function`
```python
def div(a, b):
    return a/b

expect(div).when.apply(1,2).to.have.result(1/2)
expect(div).when.apply(1,0).to.throw()
```

### assert `exception`
```python
with expect.exception():
    assert 1 == 2
```

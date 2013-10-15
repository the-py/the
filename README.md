# The python test assertion module

Inspired by should.js and rspec

# Install
```bash
pip install the
```

# History
- 0.1.4
    1. add 'expect' keyword
    2. overwriting magic methods so you can write assertion like normal expr. E.G. 'expect(1) > 0' is a valid assertion. The
    following operation or methods are all overwritten.
        > <, <=, >, >=, ==, !=, `__contains__`, `__getitem__`, `__iter__`

```python
the(1).lg(0)
the(1) > 0
expect(1).to > 0

the(1) in range(1, 3)
the(1).within(range(1, 3))
expect(1).to.be in range(1, 3)

x = {a: 1, b: 2}
the(x)['a'] == 1
the(x['a']) == 1
expect(x['a']).to.eq(1)

for i in range(1, 3):
    the(i) > 0
for i in the(range(1, 3)):
    i.should > 0
```

- 0.0.4
    1. initial

# Usage
```python
# the and expect are IDENTICAL.
from the import the, expect
```

# API
## matcher methods
### test `==`
```python
the(1).should.be.equal(1)
the(1) == 1
expect(1).to == (1)
```

### test `isinstance`
```python
the(1).should.be.an(int)
the((1,2,3)).should.be.a(tuple)
```

### test `is`
```python
the(None).Is(None)
the([1,2,3]).is_not([1,2,3])
```

### test `>`
```python
the(1).should.be.above(0)
```

### test `<`
```python
the(0).should.be.below(1)
```

### test match string
```python
the('a small module for testing').should.match('module')
```

### test `len`
```python
the([1,2,3]).should.have.length(3)
the([1,2,3]).should.have.size(3)
```

### test `in`
```python
the(1).should.In([1,2,3])
the(1).should.within([1,2,3])
expect(1) in range(1,3)
```

### test item `in` dict
```python
the({"a": 1, "b": 2}).should.have.item("a", 1)
```

### test items `in` dict
```python
the({"a": 1, "b": 2}).should.have.items(a=1, b=2)
```

### test key `in` dict
```python
the({"a": 1, "b": 2}).should.have.key("a")
```

### test keys `in` dict
```python
the({"a": 1, "b": 2}).should.have.keys("a", "b")
```

### test value `in` dict
```python
the({"a": 1, "b": 2}).should.have.value(1)
```

### test values `in` dict
```python
the({"a": 1, "b": 2}).should.have.values(1, 2)
```

### test object property
```python
class A(object):
    def __init__(self):
        self.message = 'hello world'

The(A()).should.have.property('message')
The(A()).should.have.property('message', 'hello world')
The(A()).should.have.attr('message')
The(A()).should.have.attribute('message')
```

### test object properties
```python
class A(object):
    def __init__(self):
        self.message = 'hello world'
        self.sender = 'me'
        self.receiver = 'you'

The(A()).should.have.properties('message', 'sender', 'receiver')
expect(A()).to.have.properties(sender='me', receiver='you')
```

### test object method
```python
the("hello").should.have.method("strip")
the("hello").should.respond_to("strip")
```

### test include
```python
the([1,2,3]).should.include(1)
the([1,2,3]).should.includes(1)
the([1,2,3]).should.contain(1)
the([1,2,3]).should.contains(1)
```

### test function
```python
def fib(x):
    memo = {}
    def _fib():
        if x in (0, 1): return 1
        if x not in memo: memo[x] = fib(x-2) + fib(x-1)
        return memo[x]
    return _fib()

the(fib).when.apply(1).should.Return(1)

the(fib).when.apply(1,2,3,4).should.throw()
```

### get item from dict will return an `the` object
```python
it = the({a: 1, b: 2})
it['a'] == 1
```

### when iterate through an `the` object, each item will still be an `the` object.
```python
for i in the(range(1,10)):
    i.should > 0
```

## matcher property
these property will trigger the corresponding protected matcher methods.

All the keywords
```python
coders = {'nt', 'true', 'false', 'none', 'exist',
           'ok', 'empty', 'Not', 'yes', 'exists',
           'truthy', 'falsy', 'no'}
```

### test `not`
```python
the(1).should.Not.be.a(str)
the([1,2,3]).should.nt.be.a(str)
```

### test `true`
```python
the(True).should.be.true
```

### test `false`
```python
the(False).should.be.false
```

### test `none`
```python
the(None).should.be.none
```

### test `not none`(exist)
```python
the(1).should.exist
the(1).exists
the(1).should.Not.be.none
```

### test `falsy`('', [], (), {}, False, None, 0)
```python
the([]).should.be.falsy
the('').should.be.empty
the([]).should.be.empty
the([]).should.be.no
```

### test `truthy`
```python
the(1).should.be.truthy
the(1).should.be.ok
the(1).should.be.yes
the(1).should.Not.be.empty
```

## Other buzzwords
```python
them = {'should', 'to', 'have', 'has', 'must',
        'be', 'And', 'when', 'but', 'it'}
```

these words does nothing but return the object it self.

So, instead of writing `the(1).Not.a(str)`, you write `the(1).should.Not.be.a(str).but.be.a(int)`.

Sometimes they make your assertions more readable.

Feel free to add your words if you like.
```python
the.them.add("whatever")
```

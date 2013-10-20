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

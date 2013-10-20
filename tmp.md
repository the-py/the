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
the(d).have.item(a,1)

d = {a: 1, b: 2}
the(d).have.item(a,1)
```

### assert `dict.key`

### assert `dict.value`

### assert `property`

### assert `method`

### assert `function`

### assert `exception`

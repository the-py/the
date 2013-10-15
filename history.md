# History
- 0.1.4
    1. add `expect' keyword
    2. overwriting magic methods so you can write assertion like normal exprs. E.G. `expect(1) > 0' is a valid assertion. The
    following operation or methods are all overwritten.
        > >, >=, <, <=, ==, !=, __contains__, __getitem__, __iter__
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

# python test in more verbal way

Inspired by should.js

# Example

```python
def iraise(x):
    raise Exception(x)

def fib(x):
    memo = {}
    def _fib():
        if x == 0: return 0
        if x == 1: return 1
        if x not in memo: memo[x] = fib(x-2) + fib(x-1)
        return memo[x]
    return _fib()


with The(iraise) as it:
    it.apply('hello world').should.throw('hello world')
    it.apply('hell world').should.Not.throw('hello world').but.throw('hell.*')

The(fib).when.apply(1).should.Return(1).And.when.apply(2).it.should.Return(1)

The(iraise).when.apply('hello world').should.throw('hello world')

The(iraise).when.apply('hell world').should.nt.throw('hello world').but.throw('hell.*')

The({'a': 1, 'b': 2}).should.have.items('a', b=2)
```


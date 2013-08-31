from __init__ import The

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

it = The(fib)
it.when.apply(1).should.Return(1)
it.when.apply(3).should.Return(2)

with The(fib) as it:
    it.when.apply(1).should.Return(2)

The(fib).when.apply(1).should.Return(1).And.when.apply(3).should.Return(2)

with The(iraise) as it:
    # it.apply('hell world').should.throw('ell.*')
    it.apply('hello world').should.throw('hello word')
    it.apply('hell world').should.Not.throw('hell world').but.throw('1hell')

The(iraise).when.apply('hello world').should.throw('hello world')

# The(iraise).when.apply('hell world').should.nt.throw('hello world').but.throw('hell')

The({'a': 1, 'b': 2}).should.have.items('a', b=2)

The(1).should.Not.be.an(str)

The(1).should.nt.be.an(str)

The(1).Is(1)

class A(object):
    def __init__(self):
        self.x = 1

    def __get__(self, instance, owner):
        # self.x = 0
        # return self
        return 10

class B(object):
    a = A()



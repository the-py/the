from world import World
from the import The
from context import skip
from description import Description

World().enter()

def iraise(x):
    raise Exception(x)

def fib(x):
    memo = {}
    def _fib():
        if x in (0, 1): return 1
        if x not in memo: memo[x] = fib(x-2) + fib(x-1)
        return memo[x]
    return _fib()

it = The(fib)
it.when.apply(12).should.Return(1)
it.when.apply(3).should.Return(2)

with Description("The fib function"):
    with The(fib) as it:
        it("should return some thing").when.apply(1).should.Return(1)
        it("should return some thing").when.apply(1).should.Return(321)

The(fib)("author : wenjun.yan").when.apply(1).should.Return(1).And.when.apply(3).should.Return(2)

with The(iraise) as it:
    skip()
    it.apply('hell world').should.throw('ell.*')
    it.apply('hello world').should.throw('hello word')
    it.apply('hell world').should.Not.throw('hell world').but.throw('1hell')

The(iraise).when.apply('hello world').should.throw('hello world')

World().leave()

# The(iraise).when.apply('hell world').should.nt.throw('hello world').but.throw('hell')

# The({'a': 1, 'b': 2}).should.have.items('a', b=2)

# The(1).should.Not.be.a(str)

# The(1).should.nt.be.a(str)

# The(1).Is(1)

# World().leave()

# with World("my app"):
#     with Desc("UserConstroller"):
#         it.should.respond_to("user")
#         it.should.respond_to("password")

#         with The(UserController.user) as it:
#             it.when.apply(1,2,3).should.Return(2)
#             it.when.apply(1,2,3).should.Return(2)

#         with The(UserController.password) as it:
#             it.when.apply(1).should.Return

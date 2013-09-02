from the import *
from termcolor import cprint
import time


def iraise(x):
    raise Exception(x)

def fib(x):
    memo = {}
    def _fib():
        if x in (0, 1): return 1
        if x not in memo: memo[x] = fib(x-2) + fib(x-1)
        return memo[x]
    return _fib()

World().begin()

it = The(fib)
with Description("Test fibonacci function with some random args."):
    with The(fib) as it:
        it("should return 1").when.apply(1).should.Return(1)
        it.when.apply(1).should.Return(22222222)
        it("should return 321").when.apply(1).should.Return(321)
        it("should return 121").when.apply(1).should.Return(121)

with Description("Test dictionary."):
    with The({"a": 1, "b": 2}) as it:
        with Description("check keys and values"):
            it.should.have.value("1").And.have.value("value")
            print x
            it.has.key("a").And.has.key("xx")


The(fib)("author : wenjun.yan").when.apply(1).should.Return(21)

World().leave()


from src import *
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
with Description("Test fibonacci function with some random args "):
    with It("should return the right answer", The(fib)) as it:
        it.when.apply(1).should.Return(1)
        it.when.apply(1,2,3, a=1, b=2).should.Return(22222222)
        it.when.apply(1).should.Return(321)
        it.when.apply(1).should.Return(121)

World().leave()


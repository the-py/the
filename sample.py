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

with Description("Test fibonacci function with some random args "):
    with It("should return the right answer", The(fib)) as it:
        it.when.apply(1).should.Return(1)
        assert True
        # it.when.apply(1,2,3, a=1, b=2).should.Return(22222222)
        # it.when.apply(1).should.Return(321)
        # it.when.apply(1).should.Return(121)

with Description("default assert statment"):
    with It.skip("should work"):
        assert False, 'action!'

    with Description(" just kidding"):
        with It("should be True"):
            assert False, 'action....'

World().done()

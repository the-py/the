import unittest
from helper import world, the, safe, ok, reset

class TestTheMatchers(unittest.TestCase):
    def setUp(self):
        self.eq = self.assertEqual
        self.neq = self.assertNotEqual
        self.true = self.assertTrue

    @safe
    def test_equal(self):
        the(1).equal(1)
        self.true(ok())
        reset()
        the(None).equal(None)
        self.true(ok())
        reset()
        the("a").equal(None)
        self.true(not ok())

    @safe
    def test_a(self):
        the("1").should.be.a(str)
        self.true(ok())
        reset()
        the(1).should.be.a(str)
        self.true(not ok())

    @safe
    def test_Is(self):
        the(1).Is(1)
        self.true(ok())
        reset()
        the(True).Is(False)
        self.true(not ok())

    @safe
    def test_within(self):
        the(1).within(range(1,3))
        self.true(ok())
        reset()
        the(1).within(range(1,3))
        self.true(ok())
        reset()
        the(1).within(range(2,10))
        self.true(not ok())

    @safe
    def test_above(self):
        the(1).above(0)
        self.true(ok())
        reset()
        the(1).above(1)
        self.true(not ok())

    @safe
    def test_below(self):
        the(1).below(2)
        self.true(ok())
        reset()
        the(1).below(0)
        self.true(not ok())

    @safe
    def test_match(self):
        the("what's this?").match("what.*")
        self.true(ok())
        reset()
        the("what's this?").match("xxx")
        self.true(not ok())

    @safe
    def test_length(self):
        the([1,2,3,4]).length(4)
        self.true(ok())
        reset()
        the([1,2,3,4]).length(2)
        self.true(not ok())

    @safe
    def test_item(self):
        d = {"a": 1, "b": 2, "c": 3}
        the(d).have.item("a", 1)
        self.true(ok())
        reset()
        the(d).have.item("a", 2)
        self.true(not ok())

    @safe
    def test_key(self):
        d = {"a": 1, "b": 2, "c": 3}
        the(d).have.key("a")
        self.true(ok())
        reset()
        the(d).have.key("ax")
        self.true(not ok())

    @safe
    def test_value(self):
        d = {"a": 1, "b": 2, "c": 3}
        the(d).have.value(3)
        self.true(ok())
        reset()
        the(d).have.value("123")
        self.true(not ok())

    @safe
    def test_items(self):
        d = {"a": 1, "b": 2, "c": 3}
        the(d).have.items(a=1, b=2)
        self.true(ok())
        reset()
        the(d).have.items(a=1, c=2)
        self.true(not ok())

    @safe
    def test_keys(self):
        d = {"a": 1, "b": 2, "c": 3}
        the(d).have.keys("a", "c")
        self.true(ok())
        reset()
        the(d).have.keys("b", "d")
        self.true(not ok())

    @safe
    def test_values(self):
        d = {"a": 1, "b": 2, "c": 3}
        the(d).have.values(1,2,3)
        self.true(ok())
        reset()
        the(d).have.values(4)
        self.true(not ok())

    @safe
    def test_property(self):
        class A(object):
            a = 1

        the(A).has.property("a")
        self.true(ok())
        reset()
        the(A).has.property("x")
        self.true(not ok())

    def test_include(self):
        l = [1,2,3,4]
        the(l).should.include(3)
        self.true(ok())
        reset()
        the(l).should.include(12)
        self.true(not ok())

    def test_apply(self):
        it = the(len)
        it.apply([1,2,3])
        self.eq(it.args, [([1,2,3],), {}])

    def test_return(self):
        it = the(len)
        it.apply([1,2,3]).should.Return(3)
        self.true(ok())
        reset()
        it.apply([1,2,3]).should.Return(1)
        self.true(not ok())

    def test_throw(self):
        def ex():
            raise TypeError("what??")

        the(ex).throw("what")
        self.true(ok())
        reset()
        the(ex).throw("lol", TypeError)
        self.true(not ok())

    def respond_to(self):
        the("str").should.respond_to("strip")
        self.true(ok())
        reset()
        the("str").should.respond_to("len")
        self.true(not ok())

if __name__ == '__main__':
    unittest.main()

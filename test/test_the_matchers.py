import unittest
from helper import the

class TestTheMatchers(unittest.TestCase):
    def setUp(self):
        self.eq = self.assertEqual
        self.neq = self.assertNotEqual
        self.true = self.assertTrue
        self.false = self.assertFalse
        self.r = self.assertRaises

    def test_equal(self):
        self.true(the(1).equal(1))
        self.true(the(None).equal(None))
        with self.r(Exception):
            the("a").equal(None)

    def test_a(self):
        self.true(the("1").should.be.a(str))
        with self.r(Exception):
            the(1).should.be.a(str)

    def test_Is(self):
        self.true(the(1).Is(1))
        with self.r(Exception):
            the(True).Is(False)

    def test_within(self):
        self.true(the(1).within(range(1,3)))
        with self.r(Exception):
            the(1).within(range(2,10))

    def test_above(self):
        self.true(the(1).above(0))
        with self.r(Exception):
            the(1).above(1)

    def test_below(self):
        self.true(the(1).below(2))
        with self.r(Exception):
            the(1).below(0)

    def test_match(self):
        self.true(the("what's this?").match("what.*"))
        with self.r(Exception):
            the("what's this?").match("xxx")

    def test_length(self):
        self.true(the([1,2,3,4]).length(4))
        with self.r(Exception):
            the([1,2,3,4]).length(2)

    def test_item(self):
        d = {"a": 1, "b": 2, "c": 3}
        self.true(the(d).have.item("a", 1))
        with self.r(Exception):
            the(d).have.item("a", 2)

    def test_key(self):
        d = {"a": 1, "b": 2, "c": 3}
        self.true(the(d).have.key("a"))
        with self.r(Exception):
            the(d).have.key("ax")

    def test_value(self):
        d = {"a": 1, "b": 2, "c": 3}
        self.true(the(d).have.value(3))
        with self.r(Exception):
            the(d).have.value("123")

    def test_items(self):
        d = {"a": 1, "b": 2, "c": 3}
        self.true(the(d).have.items(a=1, b=2))
        with self.r(Exception):
            the(d).have.items(a=1, c=2)

    def test_keys(self):
        d = {"a": 1, "b": 2, "c": 3}
        self.true(the(d).have.keys("a", "c"))
        with self.r(Exception):
            the(d).have.keys("b", "d")

    def test_values(self):
        d = {"a": 1, "b": 2, "c": 3}
        self.true(the(d).have.values(1,2,3))
        with self.r(Exception):
            the(d).have.values(4)

    def test_property(self):
        class A(object):
            a = 1

        self.true(the(A).has.property("a"))
        with self.r(Exception):
            the(A).has.property("x")

    def test_include(self):
        l = [1,2,3,4]
        self.true(the(l).should.include(3))
        with self.r(Exception):
            the(l).should.include(12)

    def test_apply(self):
        it = the(len)
        it.apply([1,2,3])
        self.eq(it.args, [([1,2,3],), {}])

    def test_return(self):
        it = the(len)
        self.true(it.apply([1,2,3]).should.Return(3))
        with self.r(Exception):
            it.apply([1,2,3]).should.Return(1)

    def test_throw(self):
        def ex():
            raise TypeError("what??")

        self.true(the(ex).throw("what"))
        with self.r(Exception):
            the(ex).throw("lol", TypeError)

    def respond_to(self):
        self.true(the("str").should.respond_to("strip"))
        with self.r(Exception):
            the("str").should.respond_to("len")

if __name__ == '__main__':
    unittest.main()

import unittest
from the import *


class TestTheMatchers(unittest.TestCase):
    def setUp(self):
        self.eq = self.assertEqual
        self.neq = self.assertNotEqual
        self.true = self.assertTrue
        self.false = self.assertFalse
        self.r = self.assertRaises

    def test_equal(self):
        self.true(the(1).equal(1))
        with self.r(AssertionError):
            the("a").equal("b")

    def test_a(self):
        self.true(the("1").should.be.a(str))
        with self.r(AssertionError):
            the(1).should.be.a(str)

    def test_within(self):
        self.true(the(1).within(range(1, 3)))
        with self.r(AssertionError):
            the(1).within(range(2, 10))

    def test_above(self):
        self.true(the(1).above(0))
        with self.r(AssertionError):
            the(1).above(1)

    def test_below(self):
        self.true(the(1).below(2))
        with self.r(AssertionError):
            the(1).below(0)

    def test_match(self):
        self.true(the("what's this?").match("what.*"))
        with self.r(AssertionError):
            the("what's this?").match("xxx")

    def test_length(self):
        self.true(the([1, 2, 3, 4]).length(4))
        with self.r(AssertionError):
            the([1, 2, 3, 4]).length(2)

    def test_item(self):
        d = {"a": 1, "b": 2, "c": 3}
        self.true(the(d).item(a=1))
        with self.r(AssertionError):
            the(d).have.item(a=2)

    def test_key(self):
        d = {"a": 1, "b": 2, "c": 3}
        self.true(the(d).have.key("a"))
        with self.r(AssertionError):
            the(d).have.key("ax")

    def test_value(self):
        d = {"a": 1, "b": 2, "c": 3}
        self.true(the(d).have.value(3))
        with self.r(AssertionError):
            the(d).have.value("123")

    def test_items(self):
        d = {"a": 1, "b": 2, "c": 3}
        self.true(the(d).have.items(a=1, b=2))
        with self.r(AssertionError):
            the(d).have.items(a=1, c=2)

    def test_keys(self):
        d = {"a": 1, "b": 2, "c": 3}
        self.true(the(d).have.keys("a", "c"))
        with self.r(AssertionError):
            the(d).have.keys("b", "d")

    def test_values(self):
        d = {"a": 1, "b": 2, "c": 3}
        self.true(the(d).have.values(1, 2, 3))
        with self.r(AssertionError):
            the(d).have.values(4)

    def test_property(self):
        class A(object):
            a = 1

        self.true(the(A).should.have.property("a"))
        with self.r(AssertionError):
            the(A).should.have.property("x")

    def test_properties(self):
        class A(object):
            a = 1
            b = 2

        self.true(the(A).should.have.properties(a=1, b=2))
        with self.r(AssertionError):
            the(A).should.have.properties(a=1, b=3)

    def test_include(self):
        l = [1, 2, 3, 4]
        self.true(the(l).should.include(3))
        with self.r(AssertionError):
            the(l).should.include(12)

    def test_apply(self):
        it = the(len)
        it.apply([1, 2, 3])
        self.eq(it.args, [([1, 2, 3], ), {}])

    def test_result(self):
        it = the(len)
        self.true(it.apply([1, 2, 3]).should.have.result(3))
        with self.r(AssertionError):
            it.apply([1, 2, 3]).should.have.result(1)

    def test_throw(self):
        def ex():
            raise TypeError("what??")

        self.true(the(ex).throw("what"))
        with self.r(AssertionError):
            the(ex).throw("lol", TypeError)

    def test_method(self):
        self.true(the("str").should.have.method("strip"))
        with self.r(AssertionError):
            the("str").should.have.method("len")

if __name__ == '__main__':
    unittest.main()

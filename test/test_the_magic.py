import unittest
from the import *


class TestTheMagic(unittest.TestCase):
    def setUp(self):
        self.true = self.assertTrue
        self.false = self.assertFalse
        self.r = self.assertRaises

    def test_eq(self):
        self.true(the(1) == 1)
        with self.r(AssertionError):
            the("a") == "x"

    def test_gt(self):
        self.true(the(1) > 0)
        with self.r(AssertionError):
            the(1) > 1

    def test_lt(self):
        self.true(the(1) < 2)
        with self.r(AssertionError):
            the(1) < 0

    def test_ge(self):
        self.true(the(2) >= 2)
        self.true(the(3) >= 2)
        with self.r(AssertionError):
            the(1) >= 2

    def test_le(self):
        self.true(the(1) <= 1)
        self.true(the(1) <= 2)
        with self.r(AssertionError):
            the(1) <= 0

    def test_ne(self):
        self.true(the(1) != 2)
        with self.r(AssertionError):
            the(1) != 1

    def test_contains(self):
        self.true(1 in the(range(1, 3)))
        with self.r(AssertionError):
            1 in the(range(2, 10))

    def test_getitem(self):
        target = the({"a": 1, "b": 2, "c": 3})
        self.true(target["a"] == 1)
        with self.r(AssertionError):
            target["a"] == 2

        self.true(target.NOT["x"])
        with self.r(AssertionError):
            target["x"]

if __name__ == '__main__':
    unittest.main()

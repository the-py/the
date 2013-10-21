import unittest
from the import *


class TestTheExe(unittest.TestCase):
    def setUp(self):
        self.eq = self.assertEqual
        self.neq = self.assertNotEqual
        self.r = self.assertRaises
        self.true = self.assertTrue

    # ---- coders keyworld ----

    # true
    def test_true(self):
        self.true(the(True).true)
        with self.r(AssertionError):
            the(False).true

    # false
    def test_false(self):
        self.true(the(False).false)
        with self.r(AssertionError):
            the(True).false

    # NOT
    def test_should_not(self):
        self.true(the(True).should_not.be.false)
        with self.r(AssertionError):
            the(True).should_not.be.true

    # none
    def test_none_is_none(self):
        self.true(the(None).none)
        with self.r(AssertionError):
            the(1).none

    # exist
    def test_exist(self):
        self.true(the(1).exist)
        with self.r(AssertionError):
            the(None).exist

    # ok
    def test_ok(self):
        self.true(the(1).ok)
        with self.r(AssertionError):
            the([]).ok

    # emtpy
    def test_empty(self):
        self.true(the([]).empty)
        with self.r(AssertionError):
            the(1).empty

if __name__ == '__main__':
    unittest.main()

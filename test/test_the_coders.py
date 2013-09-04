import unittest
from helper import the


class TestTheCoders(unittest.TestCase):
    def setUp(self):
        self.eq = self.assertEqual
        self.neq = self.assertNotEqual
        self.r = self.assertRaises
        self.true = self.assertTrue

    # ---- coders keyworld ----

    # true
    def test_true(self):
        self.true(the(True).true)
        with self.r(Exception):
            the(False).true

    # false
    def test_false(self):
        self.true(the(False).false)
        with self.r(Exception):
            the(True).false

    # Not
    def test_not(self):
        self.true(the(True).Not.false)
        with self.r(Exception):
            the(True).Not.True

    # none
    def test_none_is_none(self):
        self.true(the(None).none)
        with self.r(Exception):
            the(1).none

    # exist
    def test_exist(self):
        self.true(the(1).exist)
        with self.r(Exception):
            the(None).exist

    # ok
    def test_ok(self):
        self.true(the(1).ok)
        with self.r(Exception):
            the([]).ok

    # emtpy
    def test_empty(self):
        self.true(the([]).empty)
        with self.r(Exception):
            the(1).empty

if __name__ == '__main__':
    unittest.main()



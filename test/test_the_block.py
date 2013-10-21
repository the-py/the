import unittest
from the import *


class TestTheBlock(unittest.TestCase):
    def setUp(self):
        self.r = self.assertRaises

    def test_block_without_arg_and_ok(self):
        with expect.exception():
            assert False

    def test_block_without_arg_and_fail(self):
        with self.r(AssertionError):
            with expect.exception():
                pass

    def test_block_with_regex_and_ok(self):
        with expect.exception("user"):
            assert False, "username"

    def test_block_with_regex_and_fail(self):
        with self.r(AssertionError):
            with expect.exception("user"):
                assert False, "name"

    def test_block_with_type_and_ok(self):
        with expect.exception(None, AssertionError):
            assert False

    def test_block_with_type_and_fail(self):
        with self.r(AssertionError):
            with expect.exception(None, ZeroDivisionError):
                assert False

if __name__ == '__main__':
    unittest.main()

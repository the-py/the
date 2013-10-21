import unittest
from the import *


class TestTheThis(unittest.TestCase):
    def setUp(self):
        self.eq = self.assertEqual

    def test_all_built_in_them_keywords(self):
        it = the(1)
        for keyword in the.this:
            self.eq(getattr(it, keyword), it)

if __name__ == '__main__':
    unittest.main()

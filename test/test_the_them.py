import unittest
from helper import world, the

class TestTheThem(unittest.TestCase):
    def setUp(self):
        self.eq = self.assertEqual
        self.neq = self.assertNotEqual

    def test_all_built_in_them_keywords(self):
        it = the(1)
        for keyword in the.them:
            self.eq(getattr(it, keyword), it)

if __name__ == '__main__':
    unittest.main()
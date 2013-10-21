import unittest
from the import the, _TheBe, _TheA


class TestTheSpecialCase(unittest.TestCase):
    def test_the_be(self):
        it = the(1)
        self.assertTrue(isinstance(it.be, _TheBe))
        self.assertEqual(it.be.should, it)

    def test_be_callable(self):
        self.assertTrue(the(1).be(1))
        with self.assertRaises(AssertionError):
            the(True).should.be(False)

    def test_the_a(self):
        it = the(1)
        self.assertTrue(isinstance(it.a, _TheA))
        self.assertEqual(it.a.should, it)

    def test_a_callable(self):
        self.assertTrue(the("1").should.be.a(str))
        with self.assertRaises(AssertionError):
            the(1).should.be.a(str)

if __name__ == '__main__':
    unittest.main()

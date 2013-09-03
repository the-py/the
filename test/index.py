import unittest
from test_the_them import TestTheThem as Them
from test_the_coders import TestTheCoders as Coders
from test_the_matchers import TestTheMatchers as Matchers

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(Them))
    suite.addTests(unittest.makeSuite(Coders))
    suite.addTests(unittest.makeSuite(Matchers))
    unittest.TextTestRunner(verbosity=2).run(suite)

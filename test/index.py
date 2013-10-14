import unittest
from test_the_them import TestTheThem as Them
from test_the_coders import TestTheCoders as Coders
from test_the_matchers import TestTheMatchers as Matchers
from test_the_magic import TestTheMagic as Magic

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(Them))
    suite.addTests(unittest.makeSuite(Coders))
    suite.addTests(unittest.makeSuite(Matchers))
    suite.addTests(unittest.makeSuite(Magic))
    unittest.TextTestRunner(verbosity=2).run(suite)

import unittest

import rule1test


discover = unittest.TestLoader()

suite = unittest.TestSuite()
suite.addTests(discover.loadTestsFromModule(rule1test))

runner = unittest.TextTestRunner()
runner.run(suite)

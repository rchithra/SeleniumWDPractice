import unittest
from unittestpackage.test_class1 import testClass1
from unittestpackage.test_class2 import testClass2

tc1 = unittest.TestLoader().loadTestsFromTestCase(testClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(testClass2)

smoke_test = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)
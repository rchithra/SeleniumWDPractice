import unittest


class testClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*#" * 30)
        print("Class1 -> Class level setup")
        print("*#" * 30)

    def setUp(self) -> None:
        print("Class1 setup")

    def test_Class1_methodA(self):
        print("Running Class1 method A")

    def test_Class1_methodB(self):
        print("Running Class1 method B")

    def tearDown(self) -> None:
        print("Class1 teardown")

    @classmethod
    def tearDownClass(cls) -> None:
        print("*#" * 30)
        print("Class1 -> Class level teardown")
        print("*#" * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)

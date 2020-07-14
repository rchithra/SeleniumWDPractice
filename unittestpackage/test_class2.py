import unittest


class testClass2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*#" * 30)
        print("Class2 -> Class level setup")
        print("*#" * 30)

    def setUp(self) -> None:
        print("Class2 setup")

    def test_Class2_methodA(self):
        print("Running Class2 method A")

    def test_Class2_methodB(self):
        print("Running Class2 method B")

    def tearDown(self) -> None:
        print("Class2 teardown")

    @classmethod
    def tearDownClass(cls) -> None:
        print("*#" * 30)
        print("Class2 -> Class level teardown")
        print("*#" * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)

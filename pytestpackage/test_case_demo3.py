import pytest

@pytest.yield_fixture()
def setUp():
    print ("Running demo3 setup")
    yield
    print("Running demo3 teardown")


def test_methodA(setUp):
    print("Running demo3 method A")


def test_methodB(setUp):
    print("Running demo3  method B")


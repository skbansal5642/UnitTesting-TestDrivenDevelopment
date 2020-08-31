import pytest


@pytest.fixture(autouse=True)
def setup1():
    print("\nSetup 1")
    yield 
    print("\nTeardown - setup 1")


@pytest.fixture()
def setup2(request):
    print("\nSetup 2")

    def teardown_a():
        print("\nTeardown A - setup 2")

    def teardown_b():
        print("Teardown B - setup 2")

    request.addfinalizer(teardown_b)
    request.addfinalizer(teardown_a)


def test1(setup1):
    print("Executing test1")
    assert True

def test2(setup2):
    print("Executing test2")
    assert True


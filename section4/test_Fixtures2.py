import pytest

@pytest.fixture(scope="session", autouse=True)
def setupSession():
    print("\nSetup Session")
    yield
    print("\nTeardow Session")

@pytest.fixture(scope="module", autouse=True)
def setupModule():
    print("\nSetup Module")
    yield
    print("\nTeardow Module")

@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("\nSetup Function")
    yield
    print("\nTeardow Function")


def test1():
    print("Executing test1")
    assert True

def test2():
    print("Executing test2")
    assert True



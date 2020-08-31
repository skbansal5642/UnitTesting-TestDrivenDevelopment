import pytest

def test_IntAssert():
    assert 1 ==1 

def test_StrAssert():
    assert "str" == "str"

def test_floatAssert():
    assert [1,2,3] == [1,2,3]

def test_dictAssert():
    assert {"1":1} == {"1":1}

def test_float():
    assert(0.1 + 0.2) == pytest.approx(0.3)

def raisesValueException():
    raise ValueError

def test_exceptio():
    with pytest.raises(ValueError):
        raisesValueException()


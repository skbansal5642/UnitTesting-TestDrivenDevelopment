import pytest

def test_approx():
    val = 0.1 + 0.2
    assert val == pytest.approx(0.3)


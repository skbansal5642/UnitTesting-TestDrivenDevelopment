from Checkout import Checkout
from Prices import Prices
from unittest.mock import MagicMock
import json
import pytest

@pytest.fixture()
def prices(monkeypatch):
    mock_json_load = MagicMock(return_value = json.loads('{"a": 1, "b": 2, "d": 4}'))
    monkeypatch.setattr("json.load", mock_json_load)

    mock_open = MagicMock(return_value = mock_json_load)
    monkeypatch.setattr("builtins.open", mock_open)

    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)

    prices = Prices("prices.json")
    return prices


@pytest.fixture()
def checkout(prices):

    checkout = Checkout()
    for item, price in prices:
        checkout.addItemPrice(item, price)
    return checkout


def test_CanCalculateTotal(checkout):
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1


def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3


def test_canAddDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.calculateTotal() == 2


def test_ExceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem("c")

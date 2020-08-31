from pytest import raises
from Prices import Prices
from unittest.mock import MagicMock
import json
import pytest

def test_atLeastOneItem(monkeypatch):

    mock_json_load = MagicMock(return_value = json.loads('{"a": 1, "b": 2, "d": 4}'))
    monkeypatch.setattr("json.load", mock_json_load)

    mock_open = MagicMock(return_value = mock_json_load)
    monkeypatch.setattr("builtins.open", mock_open)

    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)

    prices = Prices("prices.json")

    mock_json_load = MagicMock(return_value = json.loads('{}'))
    monkeypatch.setattr("json.load", mock_json_load)
    with raises(Exception):
        prices = Prices("prices.json")


        

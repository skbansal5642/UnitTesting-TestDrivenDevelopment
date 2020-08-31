import pytest
from pytest import raises
from unittest.mock import MagicMock
from LineReader import readFromFile


@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="bar")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open

    
def test_returnsCorrectString(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    result = readFromFile("foo")
    mock_open.assert_called_once_with("foo", "r")
    assert result == "bar"

    
def test_throwsExceptionWithBadFile(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with raises(Exception):
        result = readFromFile("foo")

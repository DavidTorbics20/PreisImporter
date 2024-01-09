
import pytest
import pandas as pd
from src.reader import Reader

FILEPATH = "../docs/prices.csv"


def test_class_exists():
    reader = Reader(FILEPATH)
    assert reader


def test_file_exists():
    reader = Reader(FILEPATH)
    assert reader
    assert True


def test_file_not_exists():

    wrong_file = 'dummy.csv'

    with pytest.raises(FileNotFoundError):
        reader = Reader(wrong_file)
        assert reader


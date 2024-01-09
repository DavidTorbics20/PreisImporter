
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


def test_file_content():
    reader = Reader(FILEPATH)
    df = reader.readFile()
    assert df != ''

    dummy_data = "Firma, Epoch, Wert, Währung, Börse;" \
                 "Lenzing, 170447112, 34.75, EUR, Vienna;" \
                 "Andritz, 170447131, 59.41, USD, New York;" \
                 "EVN, 170447132, 28.55, EUR, Vienna;" \
                 "EVN, 170447133, 31.18, USD, New York;"

    valid_df = pd.read_csv(dummy_data)

    assert df == valid_df


def test_data_separators():
    reader = Reader(FILEPATH)
    df = reader.readFile()
    assert df != ''

    rows = df.split(';')
    columns = rows[0].split(',')

    assert len(rows) == 5
    assert len(columns) == 5

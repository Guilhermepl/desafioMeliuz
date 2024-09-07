import unittest

from unittest import mock
import pandas as pd

from data_loader import DataLoader

class TestDataLoader(unittest.TestCase):

    @mock.patch("pandas.read_csv")
    def test_load_sales_data(self, mock_read_csv):
        mock_data = pd.DataFrame({
            "product_price": [100, 200],
            "sale_date": ["2023-01-01", "2023-02-01"],
            "product_id": [101, 102]
        })

        mock_read_csv.return_value = mock_data

        data = DataLoader.load_sales_data()
        self.assertIsInstance(data, pd.DataFrame)
        self.assertIn("product_price", data.columns)
        self.assertIn("sale_date", data.columns)

    @mock.patch("pandas.read_csv")
    def test_load_user_history(self, mock_read_csv):
        mock_history = pd.DataFrame({
            "user_id": [1, 2],
            "interaction_date": ["2023-01-01", "2023-02-01"],
            "product_id": [101, 102]
        })

        mock_read_csv.return_value = mock_history

        history = DataLoader.load_user_history()
        self.assertIsInstance(history, pd.DataFrame)
        self.assertIn("user_id", history.columns)
        self.assertIn("interaction_date", history.columns)

import pandas as pd
import unittest

from unittest import mock

from strategies import UserHistoryStrategy, PopularProductStrategy


class TestStrategies(unittest.TestCase):

    @mock.patch("strategies.DataLoader.load_sales_data")
    @mock.patch("strategies.DataProcessing.create_sales_matrix")
    def setUp(self, mock_create_sales_matrix, mock_load_sales_data):
        self.mock_sales_data = pd.DataFrame({
            "product_id": [101, 102, 103, 104],
            "product_title": ["Product A", "Product B", "Product C", "Product D"],
            "sales_per_day": [10, 20, 30, 40],
            "cluster": [1, 2, 1, 2]
        })
        mock_load_sales_data.return_value = self.mock_sales_data
        mock_create_sales_matrix.return_value = self.mock_sales_data

        self.mock_user_history = pd.DataFrame({
            "user_id": [1, 2],
            "product_id": [101, 102],
            "interaction_date": pd.to_datetime(["2023-01-01", "2023-02-01"])
        })

        self.user_history_strategy = UserHistoryStrategy()
        self.popular_product_strategy = PopularProductStrategy()

    def test_user_history_strategy(self):
        recommendations = self.user_history_strategy.recommend(1, self.mock_user_history)

        self.assertIsInstance(recommendations, list)
        self.assertEqual(recommendations, [[103, "Product C"], [101, "Product A"]])

    def test_popular_product_strategy(self):
        recommendations = self.popular_product_strategy.recommend(1, self.mock_user_history)

        self.assertIsInstance(recommendations, list)
        self.assertEqual(recommendations, [[104, "Product D"], [102, "Product B"]])

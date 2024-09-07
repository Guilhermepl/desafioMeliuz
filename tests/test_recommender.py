import unittest

from unittest import mock

from recommender import Recommender


class TestRecommender(unittest.TestCase):

    @mock.patch("recommender.Recommender.get_user_history")
    def setUp(self, mock_get_user_history):
        mock_user_history = mock.Mock()
        mock_get_user_history.return_value = mock_user_history

        self.mock_strategy_with_history = mock.Mock()
        self.mock_strategy_without_history = mock.Mock()

        self.recommender_with_history = Recommender(use_history=True)
        self.recommender_with_history.get_recommend_strategy = mock.Mock(return_value=self.mock_strategy_with_history)

        self.recommender_without_history = Recommender(use_history=False)
        self.recommender_without_history.get_recommend_strategy = mock.Mock(
            return_value=self.mock_strategy_without_history)

    def test_get_user_recommendations_with_history(self):
        self.recommender_with_history.get_user_recommendations(1)
        self.mock_strategy_with_history.recommend.assert_called_once_with(1, mock.ANY)

    def test_get_user_recommendations_without_history(self):
        self.recommender_without_history.get_user_recommendations(1)
        self.mock_strategy_without_history.recommend.assert_called_once_with(1, mock.ANY)

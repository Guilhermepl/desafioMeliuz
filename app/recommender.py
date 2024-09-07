import pandas as pd

from data_loader import DataLoader
from strategies import UserHistoryStrategy, PopularProductStrategy


class Recommender:
    def __init__(self, use_history=False):
        self.user_history = self.get_user_history(use_history)

    @staticmethod
    def get_user_history(use_history):
        return DataLoader.load_user_history() if use_history else pd.DataFrame()

    def get_recommend_strategy(self):
        return UserHistoryStrategy() if not self.user_history.empty else PopularProductStrategy()

    def get_user_recommendations(self, user_id):
        if not self.user_history.empty:
            self.user_history = self.user_history[self.user_history['user_id'] == user_id]

        strategy = self.get_recommend_strategy()

        return strategy.recommend(user_id, self.user_history)

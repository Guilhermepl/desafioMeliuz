import pandas as pd

from constants import USER_HISTORY_FILE_PATH, SALES_HISTORY_FILE_PATH


class DataLoader:
    @staticmethod
    def load_sales_data():
        data_path = SALES_HISTORY_FILE_PATH
        data = pd.read_csv(data_path)
        data["sale_date"] = pd.to_datetime(data["sale_date"], errors="coerce")

        price_bins = [0, 100, 300, 500, 1000, 1500]
        price_labels = ["0-100", "100-300", "300-500", "500-1000", "1000+"]
        data["price_range"] = pd.cut(data["product_price"], bins=price_bins, labels=price_labels)

        return data

    @staticmethod
    def load_user_history():
        history_path = USER_HISTORY_FILE_PATH
        history = pd.read_csv(history_path)
        history["interaction_date"] = pd.to_datetime(history["interaction_date"])
        return history

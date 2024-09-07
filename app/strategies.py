from data_loader import DataLoader
from clustering import DataProcessing


class RecommendationStrategy:
    def __init__(self):
        self.data = DataLoader.load_sales_data()
        self.data = DataProcessing.create_sales_matrix(self.data)

    def recommend(self, user_id, history):
        raise NotImplementedError("Subclasses devem implementar o método 'recommend'.")


class UserHistoryStrategy(RecommendationStrategy):
    def recommend(self, user_id, history):
        user_history = history[history['user_id'] == user_id]

        products_interacted = user_history['product_id'].unique()
        user_clusters = self.data[self.data['product_id'].isin(products_interacted)]['cluster'].unique()
        similar_products = self.data[self.data['cluster'].isin(user_clusters)]

        recommended_products = similar_products.sort_values(by='sales_per_day', ascending=False).drop_duplicates(
            subset=['product_id']).head(5)

        return recommended_products[['product_id', 'product_title']].values.tolist()


class PopularProductStrategy(RecommendationStrategy):
    def recommend(self, user_id, history):
        most_popular_cluster = self.data.groupby('cluster')['sales_per_day'].sum().idxmax()
        similar_products = self.data[self.data['cluster'] == most_popular_cluster]

        recommended_products = similar_products.sort_values(by='sales_per_day', ascending=False).drop_duplicates(
            subset=['product_id']).head(5)

        return recommended_products[['product_id', 'product_title']].values.tolist()

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


class DataProcessing:
    @staticmethod
    def create_sales_matrix(data):
        features = data[['product_price', 'sales_per_day', 'store_id']].dropna()

        scaler_instance = StandardScaler()
        features_scaled = scaler_instance.fit_transform(features)

        clustering_instance = KMeans(n_clusters=5, random_state=42)
        data['cluster'] = clustering_instance.fit_predict(features_scaled)

        return data

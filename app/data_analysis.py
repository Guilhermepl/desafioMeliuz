#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "../data/xpto_sales_products_mar_may_2024.csv - Página4.csv"
data = pd.read_csv(file_path)

data.head()
#%%
data.columns
#%%
data['sale_date'] = pd.to_datetime(data['sale_date'])
#%%
data.describe()
#%%
plt.figure(figsize=(10, 6))
plt.hist(data['sales_per_day'], bins=30, color='blue', alpha=0.7)
plt.title('Distribution of Sales per Day')
plt.xlabel('Sales per Day')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
#%%
sales_over_time = data.groupby('sale_date')['sales_per_day'].sum()
plt.figure(figsize=(12, 6))
sales_over_time.plot()
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()
#%%
data['sale_date'] = pd.to_datetime(data['sale_date'], errors='coerce')

price_bins = [0, 100, 300, 500, 1000, 1500]
price_labels = ['0-100', '100-300', '300-500', '500-1000', '1000+']
data['price_range'] = pd.cut(data['product_price'], bins=price_bins, labels=price_labels)

sales_by_price_range = data.groupby(['price_range', 'sale_date'])['sales_per_day'].sum().reset_index()

plt.figure(figsize=(12, 8))
sns.lineplot(x='sale_date', y='sales_per_day', hue='price_range', data=sales_by_price_range)
plt.title('Sazonalidade de Vendas por Faixa de Preço')
plt.xlabel('Data')
plt.ylabel('Total de Vendas por Dia')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
lt.show()
#%%
plt.figure(figsize=(15, 12))

for i, price_range in enumerate(price_labels):
    plt.subplot(3, 2, i+1)
    price_data = sales_by_price_range[sales_by_price_range['price_range'] == price_range]
    plt.plot(price_data['sale_date'], price_data['sales_per_day'], label=price_range, marker='o')
    plt.title(f'Vendas: Faixa de Preço {price_range}')
    plt.xlabel('Data')
    plt.ylabel('Total de Vendas por Dia')
    plt.xticks(rotation=45)
    plt.grid(True)

plt.tight_layout()
plt.show()

#%%
sales_by_price_range['sales_pct_change'] = sales_by_price_range.groupby('price_range')['sales_per_day'].pct_change() * 100

plt.figure(figsize=(15, 12))

for i, price_range in enumerate(price_labels):
    plt.subplot(3, 2, i+1) 
    price_data = sales_by_price_range[sales_by_price_range['price_range'] == price_range]
    plt.plot(price_data['sale_date'], price_data['sales_pct_change'], label=price_range, marker='o')
    plt.title(f'Variação Percentual de Vendas: Faixa de Preço {price_range}')
    plt.xlabel('Data')
    plt.ylabel('Variação Percentual (%)')
    plt.xticks(rotation=45)
    plt.grid(True)

plt.tight_layout()
plt.show()

#%%
sales_pivot = data.pivot_table(index='product_id', columns='sale_date', values='sales_per_day', fill_value=0)

product_correlation = sales_pivot.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(product_correlation, cmap="coolwarm", center=0)
plt.title('Correlação de Vendas entre Produtos')
plt.show()
#%%
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

features = data[['product_price', 'sales_per_day', 'store_id']].dropna()

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=5, random_state=42)
data['cluster'] = kmeans.fit_predict(features_scaled)

plt.figure(figsize=(12, 8))
sns.scatterplot(x='product_price', y='sales_per_day', hue='cluster', data=data, palette='Set1')
plt.title('Clusters de Produtos com Base no Preço e Vendas')
plt.xlabel('Preço do Produto')
plt.ylabel('Vendas por Dia')
plt.grid(True)
plt.tight_layout()
plt.show()
#%%

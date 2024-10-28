import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 데이터 로드 및 전처리
df = pd.read_csv('../ex_unsuper/data/Mall_Customers.csv')
data = df.iloc[:, [3, 4]].values  # Annual Income와 Spending Score만 사용

# KMeans 모델 생성 및 예측
model = KMeans(n_clusters=5, max_iter=300, random_state=0)
pred = model.fit_predict(data)

# 클러스터 별 산점도 시각화
plt.scatter(data[pred == 0, 0], data[pred == 0, 1], s=100, c='pink', label='Cluster 1')
plt.scatter(data[pred == 1, 0], data[pred == 1, 1], s=100, c='yellow', label='Cluster 2')
plt.scatter(data[pred == 2, 0], data[pred == 2, 1], s=100, c='cyan', label='Cluster 3')
plt.scatter(data[pred == 3, 0], data[pred == 3, 1], s=100, c='magenta', label='Cluster 4')
plt.scatter(data[pred == 4, 0], data[pred == 4, 1], s=100, c='orange', label='Cluster 5')

# 클러스터 중심 표시
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], s=200, c='red', marker='X', label='Centroids')

# 그래프 설정
plt.title('Clusters of customers', fontsize=20)
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.grid(True)
plt.show()
